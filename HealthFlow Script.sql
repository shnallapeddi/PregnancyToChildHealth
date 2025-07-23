create database HealthFlow;
use LifeBegins;

SHOW TABLES IN HealthFlow;

CREATE TABLE LifeBegins (
    Region_Name VARCHAR(255) NOT NULL,
    Region_Code VARCHAR(50) NOT NULL,
    Year_num FLOAT,
    Birth_rate_crude_per_1000_people FLOAT,
    Births_attended_by_skilled_health_staff_percent_of_total FLOAT,
    Cause_of_death_by_communicable_diseases FLOAT,
    Death_rate_crude_per_1000_people FLOAT,
    Hospital_beds_per_1000_people FLOAT,
    Immunization_BCG_percent_of_one_year_old_children FLOAT,
    Immunization_HepB3_percent_of_one_year_old_children FLOAT,
    Immunization_measles_second_dose FLOAT,
    Immunization_Pol3_percent_of_one_year_old_children FLOAT,
    Life_expectancy_at_birth_female_years FLOAT,
    Life_expectancy_at_birth_male_years FLOAT,
    Life_expectancy_at_birth_total_years FLOAT,
    Lifetime_risk_of_maternal_death_percent FLOAT,
    Lifetime_risk_of_maternal_death_1_in_rate_varies_by_country INT,
    Literacy_rate_Pregnant_Women FLOAT,
    Literacy_rate_adult_total_percent_of_people_ages_15_and_above FLOAT,
    Low_birthweight_babies_percent_of_births FLOAT,
    Maternal_mortality_ratio FLOAT,
    Maternal_mortality_ratio_1 FLOAT,
    Mortality_rate_infant_per_1000_live_births FLOAT,
    Mortality_rate_infant_female_per_1000_live_births FLOAT,
    Mortality_rate_infant_male_per_1000_live_births FLOAT,
    Mortality_rate_neonatal_per_1000_live_births FLOAT,
    Newborns_protected_against_tetanus FLOAT,
    Number_of_infant_deaths FLOAT,
    Number_of_infant_deaths_female FLOAT,
    Number_of_infant_deaths_male FLOAT,
    Number_of_maternal_deaths FLOAT,
    Number_of_neonatal_deaths FLOAT,
    Number_of_stillbirths FLOAT,
    Nurses_and_midwives_per_1000_people FLOAT,
    Physicians_per_1000_people FLOAT,
    Pregnant_women_receiving_prenatal_care_percent FLOAT,
    Prevalence_of_anemia_among_pregnant_women_percent FLOAT,
    Prevalence_of_anemia_among_children FLOAT,
    Prevalence_of_current_tobacco_use_pregnant_women FLOAT,
    Prevalence_of_hypertension_pregnant_women FLOAT,
    Stillbirth_rate_per_1000_total_births FLOAT,
    Total_alcohol_consumption_per_capita FLOAT,
    Vitamin_A_supplementation_coverage_rate FLOAT,
    Region_Code_Numeric FLOAT,
    Infant_Mortality_Rate_to_Birth_Rate_Ratio FLOAT,
    Birth_Death_Ratio FLOAT,
    Immunization_Efficacy FLOAT,
    Life_Expectancy_Difference FLOAT,
    Neonatal_Mortality_Rate_to_Birth_Rate_Ratio FLOAT,
    Hypertension_to_Birth_Rate_Ratio FLOAT,
    Female_to_Male_Infant_Mortality FLOAT,
    Maternal_to_Neonatal_Mortality FLOAT
);

LOAD DATA INFILE '/Users/sharanya/Downloads/DIC/phase3_processed.csv'
INTO TABLE LifeBegins
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;

SELECT * FROM LifeBegins;

SELECT COUNT(*) AS TotalRows, COUNT(DISTINCT CONCAT(Region_Name, Year_num)) AS UniqueRows
FROM LifeBegins;
