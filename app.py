import gradio as gr
import joblib
import pandas as pd

# ==========================
# Load Trained Model
# ==========================
model = joblib.load("credit_risk_model.pkl")

# ==========================
# Prediction Function
# ==========================
def predict_credit_risk(
    age,
    income,
    loan_amount,
    credit_score,
    years_experience,
    gender,
    education,
    city,
    employment_type
):

    gender_map = {"Male": 1, "Female": 0}

    education_map = {
        "High School": 0,
        "Bachelor": 1,
        "Master": 2,
        "PhD": 3
    }

    city_map = {
        "Hyderabad": 0,
        "Mumbai": 1,
        "Delhi": 2,
        "Chennai": 3,
        "Bangalore": 4
    }

    employment_map = {
        "Salaried": 0,
        "Self-Employed": 1,
        "Business": 2
    }

    input_data = pd.DataFrame([[
        age,
        income,
        loan_amount,
        credit_score,
        years_experience,
        gender_map[gender],
        education_map[education],
        city_map[city],
        employment_map[employment_type]
    ]],
    columns=[
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "YearsExperience",
        "Gender",
        "Education",
        "City",
        "EmploymentType"
    ])

    prediction = model.predict(input_data)[0]

    # Loan-to-Income Ratio
    ratio = round((loan_amount / income) * 100, 2) if income > 0 else 0

    if prediction == 1:
        return f"""
        <div style="
            padding:25px;
            border-radius:20px;
            background:linear-gradient(135deg,#22c55e,#16a34a);
            color:white;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.3);
        ">
            <h1>🎉 ✅ LOAN APPROVED</h1>
            <h2>Congratulations! 🥳</h2>
            <p>💰 Your application has a strong approval chance.</p>
            <p>📊 Credit Score: <b>{credit_score}</b></p>
            <p>💵 Income: <b>₹{income:,.0f}</b></p>
            <p>🏦 Loan Amount: <b>₹{loan_amount:,.0f}</b></p>
            <p>📈 Loan-to-Income Ratio: <b>{ratio}%</b></p>
            <h3>🚀 Financial Profile Looks Healthy!</h3>
        </div>
        """
    else:
        return f"""
        <div style="
            padding:25px;
            border-radius:20px;
            background:linear-gradient(135deg,#ef4444,#b91c1c);
            color:white;
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,0.3);
        ">
            <h1>⚠️ ❌ LOAN REJECTED</h1>
            <h2>Application Not Approved 😔</h2>
            <p>📉 Risk level appears high.</p>
            <p>📊 Credit Score: <b>{credit_score}</b></p>
            <p>💵 Income: <b>₹{income:,.0f}</b></p>
            <p>🏦 Loan Amount: <b>₹{loan_amount:,.0f}</b></p>
            <p>📈 Loan-to-Income Ratio: <b>{ratio}%</b></p>
            <h3>💡 Improve your credit profile and try again.</h3>
        </div>
        """

# ==========================
# Custom CSS
# ==========================
custom_css = """
body{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.gradio-container{
    max-width:1100px !important;
}

footer{
    visibility:hidden;
}

h1,h2,h3{
    text-align:center;
}

.block{
    border-radius:20px !important;
}
"""

# ==========================
# Interface
# ==========================
with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="violet"
    ),
    css=custom_css
) as app:

    gr.Markdown("""
    # 💳 AI Credit Risk Prediction System

    ### 🤖 Smart Loan Eligibility Checker
    ### ⚡ Powered by Machine Learning

    ---
    #### 🔍 Fill in your details below to check your loan approval chances instantly.
    ---
    """)

    with gr.Row():

        with gr.Column():

            age = gr.Slider(
                18, 70,
                value=25,
                label="👤 Age"
            )

            income = gr.Number(
                label="💵 Annual Income (₹)",
                value=500000
            )

            loan_amount = gr.Number(
                label="🏦 Loan Amount (₹)",
                value=200000
            )

            credit_score = gr.Slider(
                300, 900,
                value=700,
                label="📊 Credit Score"
            )

            years_experience = gr.Slider(
                0, 40,
                value=5,
                label="💼 Work Experience (Years)"
            )

        with gr.Column():

            gender = gr.Radio(
                ["Male", "Female"],
                label="🚻 Gender"
            )

            education = gr.Dropdown(
                ["High School", "Bachelor", "Master", "PhD"],
                label="🎓 Education Level"
            )

            city = gr.Dropdown(
                ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Bangalore"],
                label="🌍 City"
            )

            employment_type = gr.Radio(
                ["Salaried", "Self-Employed", "Business"],
                label="🏢 Employment Type"
            )

    gr.Markdown("### 🚀 Click below to analyze your credit profile")

    predict_btn = gr.Button(
        "💳 Predict Loan Status",
        variant="primary",
        size="lg"
    )

    result = gr.HTML()

    predict_btn.click(
        predict_credit_risk,
        inputs=[
            age,
            income,
            loan_amount,
            credit_score,
            years_experience,
            gender,
            education,
            city,
            employment_type
        ],
        outputs=result
    )

    gr.Markdown("""
    ---
    ## 📌 Credit Approval Tips

    ✅ Maintain a Credit Score above 700  
    ✅ Keep a Stable Income Source  
    ✅ Increase Work Experience  
    ✅ Avoid Multiple Active Loans  
    ✅ Pay EMIs on Time  
    ✅ Maintain a Healthy Loan-to-Income Ratio  

    ---

    ### 🌟 Features

    🤖 Machine Learning Prediction  
    📊 Real-Time Risk Analysis  
    💳 Loan Approval Assessment  
    ⚡ Fast & Accurate Results  
    🎨 Modern Interactive Dashboard  

    ---

    ### ❤️ Developed with Python, Gradio & Machine Learning

    🚀 Predict • Analyze • Approve • Grow
    """)

# Launch App
app.launch()
