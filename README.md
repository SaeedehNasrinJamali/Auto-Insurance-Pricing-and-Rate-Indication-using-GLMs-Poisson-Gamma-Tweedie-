# Auto-Insurance-Pricing-and-Rate-Indication-using-GLMs-Poisson-Gamma-Tweedie-
Auto Insurance Pricing and Rate Indication using GLMs (Poisson–Gamma–Tweedie)

This project builds a Generalized Linear Model (GLM)–based pricing framework for an auto insurance portfolio using the Spain Auto Insurance dataset.
The objective is to estimate indicated pure premiums by modeling claim frequency (Poisson), severity (Gamma), and a combined Tweedie model for total annual claim costs.
The results are used to evaluate rate adequacy, analyze risk relativities, and identify rating factors that influence premiums across driver, vehicle, and regional segments.

This project demonstrates a complete actuarial modeling workflow—from data preparation to statistical modeling and diagnostics in Python, with interpretation aligned to P&C pricing practices.
#
Data
| **Category**                     | **Columns**                                                                                                     | **Description **                                                                                                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Target (Dependent Variable)**  | `Cost_claims_year`, `N_claims_year`                                                                             | Used to compute `Severity`. Only include records where `N_claims_year > 0`.                                                                                                                    |
| **Vehicle Characteristics**      | `Power`, `Cylinder_capacity`, `Value_vehicle`, `N_doors`, `Type_fuel`, `Length`, `Weight`, `Year_matriculation` | Describe the physical and mechanical properties of the insured vehicle. Larger, more powerful, or newer vehicles tend to have higher claim severity due to higher repair or replacement costs. |
| **Driver Characteristics**       | `Date_birth`, `Date_driving_licence`, `Second_driver`, `Seniority`                                              | Represent policyholder attributes. From these, `Age` and `Driving_experience` can be derived—both are relevant predictors of claim cost.                                                       |
| **Risk and Regional Factors**    | `Type_risk`, `Area`                                                                                             | Capture geographic and underwriting risk categories. These categorical features are typically strong drivers of differences in claim severity.                                                 |
| **Policy Factors**               | `Distribution_channel`, `Policies_in_force`, `Payment`, `Premium`                                               | Reflect policy-level characteristics that may influence claim handling, pricing, or settlement amounts.                                                                                        |
| **Historical Claim Information** | `N_claims_history`, `R_Claims_history`                                                                          | Indicate past claim experience, which can correlate with future claim severity or policyholder risk behavior.                                                                                  |

