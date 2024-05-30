CREATE TABLE diabetes_data (
    Age NUMERIC,
    Sex NUMERIC,
    HighChol NUMERIC,
    CholCheck NUMERIC,
    BMI NUMERIC,
    Smoker NUMERIC,
    HeartDiseaseorAttack NUMERIC,
    PhysActivity NUMERIC,
    Fruits NUMERIC,
    Veggies NUMERIC,
    HvyAlcoholConsump NUMERIC,
    GenHlth NUMERIC,
    MentHlth NUMERIC,
    PhysHlth NUMERIC,
    DiffWalk NUMERIC,
    Stroke NUMERIC,
    HighBP NUMERIC,
    Diabetes NUMERIC
);

select * from diabetes_data

CREATE TABLE hypertension_data (
    age NUMERIC,
    sex NUMERIC,
    cp NUMERIC,
    trestbps NUMERIC,
    chol NUMERIC,
    fbs NUMERIC,
    restecg NUMERIC,
    thalach NUMERIC,
    exang NUMERIC,
    oldpeak NUMERIC,
    slope NUMERIC,
    ca NUMERIC,
    thal NUMERIC,
    target NUMERIC
);

select * from hypertension_data

CREATE TABLE stroke_data (
    sex NUMERIC,
    age NUMERIC,
    hypertension NUMERIC,
    heart_disease NUMERIC,
    ever_married NUMERIC,
    work_type NUMERIC,
    Residence_type NUMERIC,
    avg_glucose_level NUMERIC,
    bmi NUMERIC,
    smoking_status NUMERIC,
    stroke NUMERIC
);

select * from stroke_data