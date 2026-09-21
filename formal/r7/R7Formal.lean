import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace R7

noncomputable def residualRent (d v : ℝ) : ℝ :=
  d * ((5 - 4 * v) * d + 2 * (1 - 4 * v)) / (32 * (1 - v)^2)

theorem FV1_zeroNetworkGapNegative
    (c : ℝ) (hc0 : 0 < c) (hc1 : c < (1 : ℝ) / 3) :
    c * (13 * c - 6) / 32 < 0 := by
  have hlin : 13 * c - 6 < 0 := by
    nlinarith
  have hmul : c * (13 * c - 6) < 0 :=
    mul_neg_of_pos_of_neg hc0 hlin
  have h32 : (0 : ℝ) < 32 := by norm_num
  exact div_neg_of_neg_of_pos hmul h32

theorem residualNumeratorStrictlyIncreasing
    (d₁ d₂ v : ℝ)
    (hd₁ : 0 ≤ d₁) (hdd : d₁ < d₂)
    (hv0 : 0 ≤ v) (hv1 : v < (1 : ℝ) / 4) :
    d₁ * ((5 - 4 * v) * d₁ + 2 * (1 - 4 * v))
      <
    d₂ * ((5 - 4 * v) * d₂ + 2 * (1 - 4 * v)) := by
  have ha : 0 < 5 - 4 * v := by nlinarith
  have hb : 0 < 2 * (1 - 4 * v) := by nlinarith
  have hd₂ : 0 < d₂ := by nlinarith
  have hsum : 0 < (5 - 4 * v) * (d₁ + d₂) + 2 * (1 - 4 * v) := by
    have hnonneg : 0 ≤ (5 - 4 * v) * (d₁ + d₂) := by
      have : 0 ≤ d₁ + d₂ := by nlinarith
      exact mul_nonneg ha.le this
    nlinarith
  have hfactor :
      d₂ * ((5 - 4 * v) * d₂ + 2 * (1 - 4 * v))
        - d₁ * ((5 - 4 * v) * d₁ + 2 * (1 - 4 * v))
      =
      (d₂ - d₁) * ((5 - 4 * v) * (d₁ + d₂) + 2 * (1 - 4 * v)) := by
    ring
  have hpos :
      0 < (d₂ - d₁) * ((5 - 4 * v) * (d₁ + d₂) + 2 * (1 - 4 * v)) :=
    mul_pos (sub_pos.mpr hdd) hsum
  nlinarith [hfactor, hpos]

theorem FV2_residualRentStrictlyIncreasing
    (d₁ d₂ v : ℝ)
    (hd₁ : 0 ≤ d₁) (hdd : d₁ < d₂)
    (hv0 : 0 ≤ v) (hv1 : v < (1 : ℝ) / 4) :
    residualRent d₁ v < residualRent d₂ v := by
  have hden : 0 < 32 * (1 - v)^2 := by
    have hvlt : v < 1 := by nlinarith
    positivity
  unfold residualRent
  apply (div_lt_div_iff_of_pos_right hden).2
  exact residualNumeratorStrictlyIncreasing d₁ d₂ v hd₁ hdd hv0 hv1

theorem FV3_postGapNegative
    (D R : ℝ) (hD : 0 < D) (hR : R < D) :
    -D + R < 0 := by
  linarith

theorem FV4_preferenceEffect
    (E D R : ℝ)
    (hED : D < E) (hD : 0 < D) (hR : R < D) :
    0 < E - D ∧ 0 < E - R ∧ -D + R < 0 := by
  constructor
  · linarith
  constructor
  · linarith
  · linarith

def StrictBlock2 (old₁ old₂ new₁ new₂ : ℝ) : Prop :=
  old₁ < new₁ ∧ old₂ < new₂

def WeakBlock2 (old₁ old₂ new₁ new₂ : ℝ) : Prop :=
  old₁ ≤ new₁ ∧ old₂ ≤ new₂ ∧ (old₁ < new₁ ∨ old₂ < new₂)

theorem FV5_indifferenceSeparatesBlockingRules
    (x y z : ℝ) (hyz : y < z) :
    WeakBlock2 x y x z ∧ ¬ StrictBlock2 x y x z := by
  constructor
  · exact ⟨le_rfl, le_of_lt hyz, Or.inr hyz⟩
  · intro h
    exact (lt_irrefl x) h.1

#print axioms FV1_zeroNetworkGapNegative
#print axioms FV2_residualRentStrictlyIncreasing
#print axioms FV3_postGapNegative
#print axioms FV4_preferenceEffect
#print axioms FV5_indifferenceSeparatesBlockingRules

end R7
