import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import brentq
import random

st.set_page_config(page_title="Debt Financing Lab", page_icon="🏦", layout="wide")

def pct(x, d=4): return f"{round(x, d)}%"
def currency(x): return f"₹{x:,.2f}"

st.title("🏦 Experiential Learning Lab: Debt Financing")
st.markdown("""
Welcome to the **Debt Financing Learning Platform**.

This app covers every aspect of how firms raise debt capital:

- Introduction to Debt Financing
- Types of Debt Instruments (Debentures, Bonds, Loans, CP, ECB)
- Term Loans vs Working Capital Finance
- Bond Valuation & Pricing
- Yield to Maturity (YTM) & Yield Measures
- Duration & Convexity
- Credit Ratings & Risk
- Covenants & Debt Contracts
- Cost of Debt (Kd) — all methods
- Debt vs Equity Financing
- Secured vs Unsecured Debt
- Fixed vs Floating Rate Debt
- External Commercial Borrowings (ECB)
- Non-Convertible Debentures (NCDs)
- Commercial Paper (CP) & Treasury Bills
- Loan Syndication
- Project Finance & Infrastructure Debt
- Debt Restructuring & IBC 2016
- Leverage Ratios & Credit Analysis
- SEBI & RBI Regulations for Debt

through:
✅ Interactive calculators  
✅ Step-by-step solvers  
✅ Real Indian corporate examples  
✅ Quiz engine  
✅ Formula cheat sheet  
✅ Case-based learning
""")

menu = st.sidebar.radio("Choose Module", [
    "Introduction",
    "Types of Debt Instruments",
    "Term Loans & Working Capital",
    "Bond Valuation",
    "Yield to Maturity (YTM)",
    "Yield Measures",
    "Duration & Convexity",
    "Credit Ratings",
    "Debt Covenants",
    "Cost of Debt (Kd)",
    "Debt vs Equity",
    "Secured vs Unsecured Debt",
    "Fixed vs Floating Rate",
    "Non-Convertible Debentures (NCDs)",
    "Commercial Paper & T-Bills",
    "External Commercial Borrowings (ECB)",
    "Loan Syndication",
    "Project Finance",
    "Debt Restructuring & IBC 2016",
    "Leverage Ratios & Credit Analysis",
    "SEBI & RBI Regulations",
    "Step-by-Step Solver",
    "AI Hint System",
    "Quiz Engine",
    "Excel Formula Trainer",
    "Formula Cheat Sheet",
    "Common Student Mistakes",
    "Advanced Quiz Bank",
    "Progress Tracker",
    "Case-Based Learning",
])

# =========================================================
if menu == "Introduction":
    st.header("📘 Introduction to Debt Financing")
    st.markdown("""
## What is Debt Financing?

Debt financing involves borrowing money that must be **repaid with interest**.
Unlike equity, it:
- Does NOT dilute ownership
- Carries **fixed interest obligations** (tax-deductible)
- Has **priority claim** in liquidation
- Creates **financial leverage**

## Why Do Firms Use Debt?
""")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("""**Tax Shield**
- Interest is tax-deductible
- Government subsidises debt
- Kd(after-tax) = Kd × (1-t)
- Cheaper than equity after tax""")
    with col2:
        st.warning("""**Leverage Benefits**
- Amplifies returns on equity
- ROE > ROA when debt costs less
- EPS rises with leverage
- Control retained by owners""")
    with col3:
        st.success("""**Market Signals**
- Debt signals confidence
- Positive signal to market
- Disciplined cash flow use
- Jensen's free cash flow theory""")

    st.markdown("""
---
## Key Indian Debt Market Facts
| Parameter | Value |
|---|---|
| India Corporate Bond Market Size | ~₹43 lakh crore (2024) |
| 10-yr G-Sec Yield | ~7.1% |
| Corporate Bond Spread over G-Sec | 50-300 bps (credit-dependent) |
| Bank Credit Growth | ~15-16% YoY (FY24) |
| Top Issuers | REC, PFC, NABARD, Reliance, HDFC |
| ECB Outstanding | ~$180 billion |
""")

# =========================================================
elif menu == "Types of Debt Instruments":
    st.header("📋 Types of Debt Instruments")
    
    instruments = pd.DataFrame({
        "Instrument": ["Term Loan", "Working Capital Loan", "Debentures/NCDs",
                       "Commercial Paper (CP)", "External Commercial Borrowing (ECB)",
                       "Treasury Bills (T-Bills)", "Government Securities (G-Sec)",
                       "Masala Bonds", "AT1 Bonds", "Subordinated Debt"],
        "Issuer": ["Firms", "Firms", "Listed Firms", "Corporates/FIs",
                   "Indian Firms", "Government", "Government",
                   "Indian Firms (abroad)", "Banks", "Banks/Firms"],
        "Maturity": ["3-15 yr", "1 yr revolving", "1-15 yr", "7-364 days",
                     "3-10 yr", "91/182/364 days", "2-40 yr",
                     "3-5 yr", "Perpetual", "5-10 yr"],
        "Secured?": ["Usually", "Usually", "Depends", "No",
                     "No", "No", "No", "No", "No", "No"],
        "Rate Type": ["Fixed/Floating", "Floating (PLR-linked)", "Fixed",
                      "Discounted", "SOFR/Fixed", "Discounted", "Fixed",
                      "Fixed (INR)", "Fixed", "Fixed"],
        "Typical Rate (India)": ["9-13%", "9-14%", "7-12%", "6.5-8%",
                                  "SOFR+200bps", "6.5-7%", "6.5-8%",
                                  "7-9%", "8-10%", "9-11%"]
    })
    st.dataframe(instruments, use_container_width=True)

    st.subheader("📊 Debt Maturity Profile")
    categories = ["Short-term (<1yr)", "Medium-term (1-5yr)", "Long-term (>5yr)"]
    instruments_by_cat = {
        "Short-term (<1yr)": ["Commercial Paper", "Cash Credit", "Overdraft", "T-Bills", "Invoice Discounting"],
        "Medium-term (1-5yr)": ["Term Loans (short)", "NCDs", "ECB (short)", "Masala Bonds"],
        "Long-term (>5yr)": ["Long-term Loans", "Infrastructure Bonds", "G-Secs", "Perpetual Bonds (AT1)"]
    }
    selected_cat = st.radio("Category", categories)
    st.success(f"**{selected_cat}:** {', '.join(instruments_by_cat[selected_cat])}")

# =========================================================
elif menu == "Term Loans & Working Capital":
    st.header("🏗️ Term Loans & Working Capital Finance")
    
    st.markdown("""
## Term Loans
Used for capital expenditure (plant, machinery, long-term assets).

**Key Features:**
- Tenure: 3-15 years
- Repayment: EMI or bullet or structured
- Security: Primary (asset) + Collateral
- Rate: Base Rate / MCLR + spread (India)
""")
    
    st.subheader("🔢 Term Loan EMI Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_amt = st.number_input("Loan Amount (₹)", value=1000000.0)
        annual_rate = st.number_input("Annual Interest Rate (%)", value=10.0)
    with col2:
        tenure_years = st.number_input("Loan Tenure (Years)", value=5, min_value=1, step=1)
        moratorium = st.number_input("Moratorium Period (Months)", value=0, min_value=0, step=1)
    with col3:
        st.markdown("**Loan Metrics:**")

    monthly_rate = annual_rate / 100 / 12
    n_months = tenure_years * 12 - moratorium

    if monthly_rate > 0 and n_months > 0:
        emi = loan_amt * monthly_rate * (1 + monthly_rate)**n_months / ((1 + monthly_rate)**n_months - 1)
        total_payment = emi * n_months
        total_interest = total_payment - loan_amt

        col1, col2, col3 = st.columns(3)
        col1.metric("Monthly EMI", currency(emi))
        col2.metric("Total Interest", currency(total_interest))
        col3.metric("Total Payment", currency(total_payment))

        # Amortisation table
        if st.checkbox("Show Amortisation Schedule"):
            amort = []
            balance = loan_amt
            for m in range(1, min(n_months+1, 61)):
                int_part = balance * monthly_rate
                prin_part = emi - int_part
                balance -= prin_part
                amort.append({"Month": m, "EMI": round(emi,2),
                               "Interest": round(int_part,2),
                               "Principal": round(prin_part,2),
                               "Balance": round(max(balance,0),2)})
            st.dataframe(pd.DataFrame(amort), use_container_width=True)

    st.divider()
    st.subheader("Working Capital Finance")
    wc_types = pd.DataFrame({
        "Facility": ["Cash Credit (CC)", "Overdraft (OD)", "Bill Discounting", "Letter of Credit (LC)", "Bank Guarantee (BG)"],
        "Purpose": ["Day-to-day operations", "Temporary shortfall", "Receivables financing", "Import/trade finance", "Performance assurance"],
        "Security": ["Inventory + Debtors", "Fixed Deposits/Assets", "Invoices", "Margins", "Margins"],
        "Rate": ["MCLR + 1-3%", "MCLR + 2-4%", "Discount rate", "Commission", "Commission"],
    })
    st.table(wc_types)

# =========================================================
elif menu == "Bond Valuation":
    st.header("💰 Bond Valuation")
    st.markdown("""
## Bond Price Formula

$$P = \\sum_{t=1}^{n} \\frac{C}{(1+r)^t} + \\frac{F}{(1+r)^n} = C \\times PVIFA(r,n) + F \\times PVIF(r,n)$$

Where: **C** = Coupon, **F** = Face value, **r** = Required return (YTM), **n** = Years to maturity
""")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        face = st.number_input("Face Value F (₹)", value=1000.0)
        coupon_rate = st.number_input("Coupon Rate (%)", value=9.0)
    with col2:
        ytm = st.number_input("Required Return / YTM (%)", value=10.0)
        n_bond = int(st.number_input("Years to Maturity", value=5, min_value=1, step=1))
    with col3:
        freq = st.radio("Coupon Frequency", ["Annual", "Semi-annual"])
    with col4:
        st.markdown("**Results:**")

    periods = n_bond if freq == "Annual" else n_bond * 2
    r_period = ytm/100 if freq == "Annual" else ytm/100/2
    coupon = face * coupon_rate/100 if freq == "Annual" else face * coupon_rate/100/2

    pvifa = (1 - (1+r_period)**(-periods)) / r_period
    pvif = 1/(1+r_period)**periods
    price = coupon * pvifa + face * pvif

    col1, col2, col3 = st.columns(3)
    col1.metric("Bond Price", currency(price))
    col2.metric("PV of Coupons", currency(coupon * pvifa))
    col3.metric("PV of Face Value", currency(face * pvif))

    if price > face:
        st.success(f"✅ PREMIUM BOND — Price (₹{round(price,2)}) > Face Value (₹{face}) because YTM < Coupon Rate")
    elif price < face:
        st.error(f"❌ DISCOUNT BOND — Price (₹{round(price,2)}) < Face Value (₹{face}) because YTM > Coupon Rate")
    else:
        st.info("PAR BOND — Price = Face Value because YTM = Coupon Rate")

    # Cash flow table
    st.subheader("📊 Cash Flow Breakdown")
    cf_data = []
    for t in range(1, periods+1):
        cf = coupon + (face if t == periods else 0)
        pv = cf/(1+r_period)**t
        cf_data.append({"Period": t, "Cash Flow (₹)": round(cf,2), "PV Factor": round(1/(1+r_period)**t,6), "PV (₹)": round(pv,2)})
    st.dataframe(pd.DataFrame(cf_data), use_container_width=True)

    # Price sensitivity
    st.subheader("📈 Bond Price vs YTM")
    ytm_range = np.arange(1, 20, 0.5)
    prices = []
    for y in ytm_range:
        r_p = y/100 if freq == "Annual" else y/100/2
        pv_a = (1-(1+r_p)**(-periods))/r_p
        pv_f = 1/(1+r_p)**periods
        prices.append(coupon*pv_a + face*pv_f)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ytm_range, y=prices, mode='lines',
                             line=dict(color='#0D3B2E', width=2), name='Bond Price'))
    fig.add_vline(x=ytm, line_dash="dash", line_color="red",
                  annotation_text=f"Current YTM={ytm}%")
    fig.add_hline(y=face, line_dash="dot", line_color="gray",
                  annotation_text=f"Face Value ₹{face}")
    fig.update_layout(title="Bond Price vs YTM (Inverse Relationship)",
                      xaxis_title="YTM (%)", yaxis_title="Bond Price (₹)")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Yield to Maturity (YTM)":
    st.header("📊 Yield to Maturity (YTM)")
    st.markdown("""
## What is YTM?

YTM is the **total return** anticipated on a bond if held to maturity.
It equates the bond's current price to the PV of all future cash flows.

## Approximation Formula

$$YTM \\approx \\frac{C + (F-P)/n}{(F+P)/2} \\times 100$$

## Exact YTM: Solve iteratively (Excel: =RATE or =YIELD)
""")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        face_ytm = st.number_input("Face Value (₹)", value=1000.0, key="ytm_f")
        coupon_ytm = st.number_input("Annual Coupon (₹)", value=90.0)
    with col2:
        price_ytm = st.number_input("Current Market Price (₹)", value=950.0)
        n_ytm = st.number_input("Years to Maturity", value=5.0)
    with col3:
        tax_ytm = st.number_input("Tax Rate (%)", value=30.0)
    with col4:
        st.markdown("**Results:**")

    # Approximation
    ytm_approx = (coupon_ytm + (face_ytm - price_ytm)/n_ytm) / ((face_ytm + price_ytm)/2) * 100
    kd_after_tax = ytm_approx * (1 - tax_ytm/100)

    # Exact YTM
    try:
        ytm_exact = brentq(
            lambda r: sum(coupon_ytm/(1+r)**t for t in range(1,int(n_ytm)+1)) + face_ytm/(1+r)**n_ytm - price_ytm,
            0.001, 0.999
        ) * 100
    except:
        ytm_exact = ytm_approx

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("YTM (Approx)", pct(ytm_approx))
    col2.metric("YTM (Exact)", pct(ytm_exact))
    col3.metric("Kd After-tax (Approx)", pct(kd_after_tax))
    col4.metric("Kd After-tax (Exact)", pct(ytm_exact*(1-tax_ytm/100)))

    st.code(f"Excel: =RATE({int(n_ytm)}, -{coupon_ytm}, {price_ytm}, -{face_ytm}) × (1-{tax_ytm/100})", language="excel")

# =========================================================
elif menu == "Yield Measures":
    st.header("📐 Bond Yield Measures")
    col1, col2, col3 = st.columns(3)
    with col1:
        face_y = st.number_input("Face Value (₹)", value=1000.0, key="ym_f")
        coupon_y = st.number_input("Annual Coupon (₹)", value=90.0, key="ym_c")
    with col2:
        price_y = st.number_input("Market Price (₹)", value=950.0, key="ym_p")
        n_y = st.number_input("Years to Maturity", value=5.0, key="ym_n")
    with col3:
        call_price = st.number_input("Call Price (₹, if callable)", value=1020.0)
        call_years = st.number_input("Years to Call", value=3.0)

    nom_yield = coupon_y / face_y * 100
    curr_yield = coupon_y / price_y * 100
    ytm_y = (coupon_y + (face_y-price_y)/n_y) / ((face_y+price_y)/2) * 100
    ytc = (coupon_y + (call_price-price_y)/call_years) / ((call_price+price_y)/2) * 100

    yields_df = pd.DataFrame({
        "Yield Measure": ["Nominal Yield (Coupon Rate)", "Current Yield", "YTM (Approx)", "Yield to Call (YTC)"],
        "Formula": ["Coupon/Face Value", "Coupon/Price", "[C+(F-P)/n]/[(F+P)/2]", "[C+(Call-P)/n]/[(Call+P)/2]"],
        "Value": [pct(nom_yield), pct(curr_yield), pct(ytm_y), pct(ytc)],
        "Meaning": [
            "Stated coupon as % of face value",
            "Annual income relative to current investment",
            "Total return if held to maturity",
            "Total return if called on call date"
        ]
    })
    st.table(yields_df)

    st.subheader("Yield Relationships")
    if price_y < face_y:
        st.success("**Discount Bond:** Nominal Yield < Current Yield < YTM")
    elif price_y > face_y:
        st.error("**Premium Bond:** Nominal Yield > Current Yield > YTM")
    else:
        st.info("**Par Bond:** Nominal Yield = Current Yield = YTM")

# =========================================================
elif menu == "Duration & Convexity":
    st.header("⏱️ Duration & Convexity")
    st.markdown("""
## Duration — Measuring Interest Rate Risk

**Macaulay Duration:** Weighted average time to receive cash flows (in years)

$$D_{mac} = \\frac{\\sum_{t=1}^{n} t \\times PV(CF_t)}{P}$$

**Modified Duration:** Price sensitivity to yield change

$$D_{mod} = \\frac{D_{mac}}{1+r}$$

**Price Change Approximation:**

$$\\frac{\\Delta P}{P} \\approx -D_{mod} \\times \\Delta y$$
""")
    col1, col2, col3 = st.columns(3)
    with col1:
        face_d = st.number_input("Face Value (₹)", value=1000.0, key="dur_f")
        coupon_d = st.number_input("Coupon Rate (%)", value=9.0, key="dur_c")
    with col2:
        ytm_d = st.number_input("YTM (%)", value=10.0, key="dur_ytm")
        n_d = int(st.number_input("Years to Maturity", value=5, min_value=1, step=1))
    with col3:
        delta_y = st.number_input("Yield Change Δy (%)", value=1.0)

    r = ytm_d/100
    coupon_amt = face_d * coupon_d/100
    price_d = sum(coupon_amt/(1+r)**t for t in range(1,n_d+1)) + face_d/(1+r)**n_d
    mac_dur = sum(t * (coupon_amt/(1+r)**t) for t in range(1,n_d+1)) / price_d
    mac_dur += n_d * (face_d/(1+r)**n_d) / price_d
    mod_dur = mac_dur / (1+r)
    pct_price_change = -mod_dur * delta_y/100 * 100

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Bond Price", currency(price_d))
    col2.metric("Macaulay Duration", f"{round(mac_dur,4)} years")
    col3.metric("Modified Duration", round(mod_dur, 4))
    col4.metric(f"Price Change for {delta_y}% yield rise", pct(pct_price_change))

    st.info(f"""
If yield rises by {delta_y}%:
- Price change ≈ {round(pct_price_change,4)}%
- New approx. price ≈ ₹{round(price_d*(1+pct_price_change/100),2)}
""")

    dur_table = pd.DataFrame({
        "Property": ["Higher Coupon Rate", "Longer Maturity", "Higher YTM", "Zero-coupon Bond"],
        "Effect on Duration": ["Lowers Duration", "Raises Duration", "Lowers Duration", "Duration = Maturity"],
        "Implication": ["Less price sensitive", "More price sensitive", "Less sensitive", "Most price sensitive"]
    })
    st.table(dur_table)

# =========================================================
elif menu == "Credit Ratings":
    st.header("⭐ Credit Ratings")
    
    ratings_df = pd.DataFrame({
        "Rating Agency": ["CRISIL (India)", "ICRA (India)", "CARE (India)", "S&P (Global)", "Moody's (Global)"],
        "Best": ["AAA", "AAA", "AAA", "AAA", "Aaa"],
        "Investment Grade": ["AA to BBB-", "AA to BBB-", "AA to BBB-", "AA to BBB-", "Aa to Baa3"],
        "Speculative": ["BB+ to D", "BB+ to D", "BB+ to D", "BB+ to D", "Ba1 to C"],
        "Default": ["D", "D", "D", "D", "C"]
    })
    st.table(ratings_df)

    st.subheader("Credit Spread Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        g_sec_rate = st.number_input("G-Sec Yield (Risk-free) %", value=7.1)
    with col2:
        rating = st.selectbox("Bond Rating", ["AAA", "AA+", "AA", "A+", "A", "BBB", "BB", "B"])
        spread_map = {"AAA": 60, "AA+": 80, "AA": 100, "A+": 130, "A": 160, "BBB": 220, "BB": 350, "B": 500}
        spread_bps = spread_map[rating]
    with col3:
        st.metric("Typical Spread (bps)", spread_bps)
        bond_yield = g_sec_rate + spread_bps/100
        st.metric("Estimated Bond Yield", pct(bond_yield))

    st.subheader("Factors Affecting Credit Rating")
    factors = pd.DataFrame({
        "Factor": ["Debt/Equity Ratio", "Interest Coverage", "Cash Flow / Debt", "Business Risk",
                   "Management Quality", "Industry Outlook", "Government Support"],
        "Higher Rating When": ["Low D/E", ">4x for AAA", ">30%", "Stable sector",
                                "Track record", "Growing sector", "PSU/Govt backing"],
        "Lower Rating When": ["High D/E", "<1.5x risks downgrade", "<10%", "Cyclical/disruptive",
                               "Management changes", "Sunset industry", "Pure private"]
    })
    st.table(factors)

# =========================================================
elif menu == "Debt Covenants":
    st.header("📜 Debt Covenants")
    st.markdown("""
## What are Covenants?

**Covenants** are contractual terms in loan/bond agreements that restrict borrower behaviour
to protect lenders.

## Types of Covenants
""")
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
**Affirmative (Positive) Covenants**
Things the borrower MUST DO:
- Maintain minimum interest coverage ratio
- Provide audited financial statements
- Maintain adequate insurance
- Notify lender of material events
- Maintain required credit rating
        """)
    with col2:
        st.warning("""
**Negative (Restrictive) Covenants**
Things the borrower CANNOT DO:
- Exceed maximum D/E ratio
- Sell major assets without approval
- Pay dividends above threshold
- Make large acquisitions without approval
- Create additional debt (pari passu)
        """)

    st.subheader("📊 Covenant Compliance Checker")
    col1, col2 = st.columns(2)
    with col1:
        ebit_cv = st.number_input("EBIT (₹ Cr)", value=500.0)
        interest_cv = st.number_input("Interest Expense (₹ Cr)", value=120.0)
        total_debt = st.number_input("Total Debt (₹ Cr)", value=2000.0)
        equity_cv = st.number_input("Total Equity (₹ Cr)", value=3000.0)
    with col2:
        min_icr = st.number_input("Covenant: Min Interest Coverage", value=3.0)
        max_de = st.number_input("Covenant: Max D/E Ratio", value=1.0)

    icr = ebit_cv / interest_cv if interest_cv > 0 else 0
    de_ratio = total_debt / equity_cv if equity_cv > 0 else 0

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Interest Coverage Ratio", round(icr, 2))
        if icr >= min_icr:
            st.success(f"✅ ICR {round(icr,2)} ≥ Covenant minimum {min_icr}")
        else:
            st.error(f"❌ COVENANT BREACH! ICR {round(icr,2)} < Minimum {min_icr}")
    with col2:
        st.metric("D/E Ratio", round(de_ratio, 2))
        if de_ratio <= max_de:
            st.success(f"✅ D/E {round(de_ratio,2)} ≤ Covenant maximum {max_de}")
        else:
            st.error(f"❌ COVENANT BREACH! D/E {round(de_ratio,2)} > Maximum {max_de}")

# =========================================================
elif menu == "Cost of Debt (Kd)":
    st.header("💸 Cost of Debt (Kd)")
    st.markdown("""
## Three Methods

### 1. Simple Method (Bond at par)
$$K_d \\text{ (after-tax)} = \\text{Coupon Rate} \\times (1-t)$$

### 2. Approximation Method
$$K_d \\text{ (pre-tax)} = \\frac{I + (RV-NP)/n}{(RV+NP)/2} \\times 100$$

### 3. YTM Method (Exact)
Excel: =RATE(n, -coupon, NP, -RV) × (1-t)
""")
    method = st.radio("Choose Method", ["Simple", "Approximation", "YTM (Exact)"])

    if method == "Simple":
        col1, col2 = st.columns(2)
        with col1:
            kd_pre = st.number_input("Pre-tax Kd / Coupon Rate (%)", value=10.0)
        with col2:
            t_s = st.number_input("Tax Rate (%)", value=30.0)
        kd_at = kd_pre*(1-t_s/100)
        st.success(f"Kd (after-tax) = {kd_pre}% × (1-{t_s}%) = **{pct(kd_at)}**")

    elif method == "Approximation":
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: I = st.number_input("Annual Interest I (₹)", value=100.0)
        with col2: RV = st.number_input("Redemption Value RV (₹)", value=1000.0)
        with col3: NP = st.number_input("Net Proceeds NP (₹)", value=960.0)
        with col4: n_a = st.number_input("Years n", value=5.0)
        with col5: t_a = st.number_input("Tax Rate (%)", value=30.0, key="approx_t")
        
        kd_pre_a = (I+(RV-NP)/n_a)/((RV+NP)/2)*100
        kd_at_a = kd_pre_a*(1-t_a/100)
        st.latex(f"K_d = \\frac{{{I}+({RV}-{NP})/{n_a}}}{{({RV}+{NP})/2}} \\times 100 = {round(kd_pre_a,4)}\\%")
        st.success(f"After-tax Kd = {round(kd_pre_a,4)}% × (1-{t_a}%) = **{pct(kd_at_a)}**")

    else:
        col1, col2, col3, col4 = st.columns(4)
        with col1: coupon_e = st.number_input("Annual Coupon (₹)", value=100.0)
        with col2: np_e = st.number_input("Net Proceeds (₹)", value=960.0)
        with col3: fv_e = st.number_input("Redemption Value (₹)", value=1000.0)
        with col4:
            n_e = int(st.number_input("Years", value=5, min_value=1, step=1))
            t_e = st.number_input("Tax Rate (%)", value=30.0, key="ytm_t")

        try:
            ytm_e = brentq(
                lambda r: sum(coupon_e/(1+r)**t for t in range(1,n_e+1)) + fv_e/(1+r)**n_e - np_e,
                0.001, 0.99
            )*100
            kd_at_e = ytm_e*(1-t_e/100)
            col1, col2 = st.columns(2)
            col1.metric("YTM (pre-tax Kd)", pct(ytm_e))
            col2.metric("After-tax Kd", pct(kd_at_e))
        except:
            st.error("Could not solve. Check inputs.")
        st.code(f"=RATE({n_e},-{coupon_e},{np_e},-{fv_e})*(1-{t_e/100})", language="excel")

# =========================================================
elif menu == "Debt vs Equity":
    st.header("⚖️ Debt vs Equity Financing")
    
    comparison = pd.DataFrame({
        "Feature": ["Repayment", "Cost", "Tax Benefit", "Risk to Firm",
                    "Dilution", "Control", "Credit Rating", "Flexibility",
                    "Signal to Market", "Suitable for"],
        "Debt": ["Mandatory (interest + principal)", "Lower (tax shield)",
                 "Yes — interest deductible", "Higher (financial risk)",
                 "None", "Retained by promoters", "Affected by high debt",
                 "Less flexible", "Positive (confidence)", "Stable CF firms"],
        "Equity": ["None (no repayment)", "Higher (no tax shield)",
                   "No (dividend post-tax)", "Lower (no fixed obligation)",
                   "Yes — dilutes owners", "Shared with new shareholders",
                   "Improves equity base", "More flexible", "Negative (overvaluation?)",
                   "Growth/uncertain CF firms"]
    })
    st.table(comparison)

    st.subheader("🔢 EBIT-EPS Impact")
    col1, col2 = st.columns(2)
    with col1:
        ebit_de = st.number_input("EBIT (₹)", value=300000.0)
        tax_de = st.number_input("Tax Rate (%)", value=30.0, key="de_tax")
    with col2:
        interest_debt = st.number_input("Interest (Debt Plan) (₹)", value=60000.0)
        shares_eq = st.number_input("Shares (Equity Plan)", value=150000.0)
        shares_debt = st.number_input("Shares (Debt Plan)", value=75000.0)

    eps_eq = ebit_de*(1-tax_de/100)/shares_eq
    eps_debt = (ebit_de-interest_debt)*(1-tax_de/100)/shares_debt

    col1, col2 = st.columns(2)
    col1.metric("EPS — Equity Plan", currency(eps_eq))
    col2.metric("EPS — Debt Plan", currency(eps_debt))

    if eps_debt > eps_eq:
        st.success(f"✅ Debt plan gives HIGHER EPS at EBIT=₹{ebit_de:,.0f}")
    else:
        st.info(f"Equity plan gives higher EPS at this EBIT level")

# =========================================================
elif menu == "Secured vs Unsecured Debt":
    st.header("🔒 Secured vs Unsecured Debt")
    
    comp_su = pd.DataFrame({
        "Feature": ["Collateral", "Interest Rate", "Priority in Liquidation",
                    "Borrower Risk", "Common For", "Examples"],
        "Secured Debt": ["Yes — specific asset pledged", "Lower (secured by assets)",
                          "First charge on pledged assets",
                          "Lower for lender", "Capex, mortgages, vehicle loans",
                          "Term loans with charge on machinery"],
        "Unsecured Debt": ["No collateral", "Higher (no asset backing)",
                            "Residual claim after secured creditors",
                            "Higher for lender", "Short-term, corporate bonds, CPs",
                            "Commercial Paper, Clean Overdraft, NCDs (unsecured)"]
    })
    st.table(comp_su)

    st.subheader("Types of Charges (India)")
    charges = pd.DataFrame({
        "Charge Type": ["Fixed Charge", "Floating Charge", "Pari Passu Charge", "Second Charge"],
        "Description": [
            "On specific identified asset (land, building)",
            "On movable assets (inventory, receivables) — crystallises on default",
            "Equal ranking with other lenders on same asset",
            "Junior to first charge; gets paid only after first charge cleared"
        ],
        "Example": ["Mortgage on factory", "Hypothecation of inventory",
                    "Multiple banks share charge equally", "Promoter second charge on plant"]
    })
    st.table(charges)

# =========================================================
elif menu == "Fixed vs Floating Rate":
    st.header("📊 Fixed vs Floating Rate Debt")
    
    comp_ff = pd.DataFrame({
        "Feature": ["Rate", "Interest expense predictability", "Benefit when rates rise",
                    "Benefit when rates fall", "Common instruments", "India benchmark"],
        "Fixed Rate": ["Locked in at issuance", "Fully predictable", "✅ Yes (locked at lower rate)",
                        "❌ No (stuck at higher rate)", "NCDs, corporate bonds, fixed deposits",
                        "G-Sec yield at time of issuance"],
        "Floating Rate": ["Resets periodically (MCLR/SOFR)", "Variable", "❌ Higher cost",
                           "✅ Benefit (rate resets lower)", "Term loans, ECBs, working capital",
                           "MCLR (India) / SOFR (USD loans)"]
    })
    st.table(comp_ff)

    st.subheader("🔢 Floating Rate Interest Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        principal = st.number_input("Principal (₹ Cr)", value=100.0)
        base_rate = st.number_input("MCLR / Base Rate (%)", value=8.5)
    with col2:
        spread = st.number_input("Spread above MCLR (%)", value=1.5)
    with col3:
        rate_change = st.number_input("Expected MCLR Change (%)", value=0.5,
                                       help="+ for rate hike, - for cut")

    current_rate = base_rate + spread
    new_rate = base_rate + rate_change + spread
    current_interest = principal * current_rate / 100
    new_interest = principal * new_rate / 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Effective Rate", pct(current_rate))
    col2.metric("New Effective Rate (after change)", pct(new_rate))
    col3.metric("Change in Annual Interest Cost", f"₹{round(new_interest-current_interest,2)} Cr")

# =========================================================
elif menu == "Non-Convertible Debentures (NCDs)":
    st.header("📄 Non-Convertible Debentures (NCDs)")
    st.markdown("""
## What are NCDs?

**NCDs** are fixed-income debt instruments issued by companies that **cannot** be converted into equity.
They are listed on NSE/BSE and tradeable.

## Key Features
| Feature | Detail |
|---|---|
| Issuer | Listed companies, NBFCs, HFCs |
| Maturity | 1-15 years |
| Interest | Fixed coupon, paid quarterly/annually |
| Security | Secured (first/second charge) or Unsecured |
| Listing | NSE/BSE (mandatory for public issue) |
| SEBI Regulation | SEBI (Issue & Listing of NCS) Regulations 2021 |
| Credit Rating | Mandatory (minimum investment grade BBB-) |
| Demat | Held in demat account |
| Liquidity | Secondary market (lower than equity) |
""")

    st.subheader("🔢 NCD Yield Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        face_ncd = st.number_input("Face Value (₹)", value=1000.0, key="ncd_f")
        coupon_ncd = st.number_input("Coupon Rate (%)", value=9.5)
    with col2:
        price_ncd = st.number_input("Current Market Price (₹)", value=980.0)
        n_ncd = st.number_input("Remaining Maturity (Years)", value=3.0)
    with col3:
        g_sec = st.number_input("Comparable G-Sec Yield (%)", value=7.1)

    coupon_amt_ncd = face_ncd * coupon_ncd/100
    ytm_ncd = (coupon_amt_ncd + (face_ncd-price_ncd)/n_ncd)/((face_ncd+price_ncd)/2)*100
    spread_ncd = ytm_ncd - g_sec

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Yield", pct(coupon_amt_ncd/price_ncd*100))
    col2.metric("YTM", pct(ytm_ncd))
    col3.metric("Credit Spread over G-Sec", f"{round(spread_ncd*100,0):.0f} bps")

    st.subheader("Public vs Private NCD")
    pub_priv = pd.DataFrame({
        "Feature": ["Process", "SEBI filing", "Investor base", "Disclosure", "Minimum size"],
        "Public NCD": ["Full public offering; SEBI DRHP", "Full DRHP filing", "All investors", "Full disclosures", "No minimum"],
        "Privately Placed NCD": ["Placed with ≤200 investors", "Simplified filing", "Institutional/HNI only", "Simplified", "Often ₹1Cr+"]
    })
    st.table(pub_priv)

# =========================================================
elif menu == "Commercial Paper & T-Bills":
    st.header("📃 Commercial Paper & Treasury Bills")

    st.subheader("Commercial Paper (CP)")
    st.markdown("""
**CP** is a short-term unsecured promissory note issued at a discount by creditworthy firms.
- Maturity: 7 days to 1 year
- Issued at discount; redeemed at face value
- CRISIL/ICRA rating A1+ required (highest short-term)
- No collateral; based on issuer's creditworthiness
- Minimum denomination: ₹5 lakh

## CP Pricing (Discount Instrument)

$$\\text{Issue Price} = \\frac{FV}{1 + r \\times \\frac{n}{365}}$$

$$\\text{Yield} = \\frac{FV - IP}{IP} \\times \\frac{365}{n} \\times 100$$
""")
    col1, col2, col3 = st.columns(3)
    with col1:
        fv_cp = st.number_input("Face Value (₹)", value=100000.0, key="cp_fv")
        n_cp = st.number_input("Days to Maturity", value=91.0)
    with col2:
        rate_cp = st.number_input("Discount Rate (%)", value=7.0, key="cp_r")
    with col3:
        st.markdown("**Results:**")

    ip_cp = fv_cp / (1 + rate_cp/100 * n_cp/365)
    discount_cp = fv_cp - ip_cp
    yield_cp = (fv_cp-ip_cp)/ip_cp * 365/n_cp * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Issue Price", currency(ip_cp))
    col2.metric("Discount Amount", currency(discount_cp))
    col3.metric("Effective Yield", pct(yield_cp))

    st.divider()
    st.subheader("Treasury Bills (T-Bills)")
    st.markdown("""
Issued by RBI on behalf of Government of India. Zero-default risk.
- 91-day, 182-day, 364-day
- Issued at discount via weekly auctions
- Most liquid money market instrument
- Used for liquidity management by banks
""")

# =========================================================
elif menu == "External Commercial Borrowings (ECB)":
    st.header("🌍 External Commercial Borrowings (ECB)")
    st.markdown("""
## What is ECB?

Indian firms can borrow in **foreign currency** from overseas lenders.
Regulated by RBI under FEMA.

## ECB Framework (RBI)

| Feature | Track I (Loans) | Track II (Bonds) |
|---|---|---|
| Eligible borrowers | Firms in infrastructure, manufacturing, services | All eligible borrowers |
| Min maturity | 3 years (up to $50M); 5 years (above $50M) | 10 years |
| Interest rate cap | Benchmark + 450 bps | Benchmark + 450 bps |
| Benchmark | SOFR / EURIBOR | SOFR / EURIBOR |
| End use | Capex, project, refinancing | Any permissible |

## ECB Cost Calculation
""")
    col1, col2, col3 = st.columns(3)
    with col1:
        sofr_rate = st.number_input("SOFR Rate (%)", value=5.3)
        ecb_spread = st.number_input("Spread over SOFR (bps)", value=200.0)
    with col2:
        inr_usd = st.number_input("INR/USD Exchange Rate", value=83.5)
        hedge_cost = st.number_input("Hedging Cost (%)", value=3.5,
                                      help="Cost of USD/INR forward contract")
    with col3:
        st.markdown("**Cost Analysis:**")

    ecb_usd_cost = sofr_rate + ecb_spread/100
    ecb_inr_cost = ecb_usd_cost + hedge_cost
    dom_loan_rate = st.number_input("Comparable Domestic Loan Rate (%)", value=10.5)

    col1, col2, col3 = st.columns(3)
    col1.metric("ECB Cost (USD)", pct(ecb_usd_cost))
    col2.metric("ECB Fully Hedged Cost (INR)", pct(ecb_inr_cost))
    col3.metric("Domestic Loan Rate", pct(dom_loan_rate))

    if ecb_inr_cost < dom_loan_rate:
        st.success(f"✅ ECB is cheaper by {round(dom_loan_rate-ecb_inr_cost,2)}% after hedging")
    else:
        st.warning(f"⚠️ ECB is costlier by {round(ecb_inr_cost-dom_loan_rate,2)}% after hedging — domestic loan preferred")

    st.warning("Key risk: If hedging is not done, INR depreciation makes ECB very expensive. Unhedged ECB = forex risk!")

# =========================================================
elif menu == "Loan Syndication":
    st.header("🤝 Loan Syndication")
    st.markdown("""
## What is Loan Syndication?

When a loan is **too large for a single bank**, multiple banks form a **syndicate**
to share the loan and the credit risk.

## Key Roles

| Role | Bank | Responsibility |
|---|---|---|
| **Lead Arranger** | Largest bank | Structures deal, negotiates terms, takes largest share |
| **Co-arranger** | Major banks | Take significant shares; may help in syndication |
| **Participant Banks** | Smaller banks | Take small shares; no deal structuring |
| **Facility Agent** | Lead bank | Administrative agent; manages loan drawdowns and repayments |
| **Security Trustee** | Separate entity | Holds security on behalf of all lenders |

## Typical Syndication Structure
""")
    total_loan = st.number_input("Total Loan Amount (₹ Cr)", value=5000.0)
    n_banks = int(st.number_input("Number of Banks in Syndicate", value=5, min_value=2, max_value=8, step=1))

    shares = [35, 25, 20, 12, 8, 6, 5, 4][:n_banks]
    shares[-1] = 100 - sum(shares[:-1])
    
    synd_df = pd.DataFrame({
        "Bank": [f"Bank {chr(65+i)}" for i in range(n_banks)],
        "Role": (["Lead Arranger"] + ["Co-arranger"]*(min(2,n_banks-2)) + ["Participant"]*(n_banks-3))[:n_banks],
        "Share (%)": shares,
        "Amount (₹ Cr)": [round(total_loan*s/100,2) for s in shares]
    })
    st.dataframe(synd_df, use_container_width=True)

    fig = go.Figure(go.Pie(labels=synd_df["Bank"], values=synd_df["Amount (₹ Cr)"], hole=0.4))
    fig.update_layout(title="Syndicate Loan Share Distribution")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Project Finance":
    st.header("🏭 Project Finance & Infrastructure Debt")
    st.markdown("""
## What is Project Finance?

**Project Finance** is debt financing where repayment depends entirely on the **project's cash flows**,
not the sponsor's balance sheet. Common in infrastructure.

## Key Features
- **Special Purpose Vehicle (SPV):** Separate entity for each project
- **Non-recourse / Limited-recourse:** Lenders can only claim project assets, not sponsor
- **Cash flow waterfall:** Priority distribution of project revenues
- **Debt Service Coverage Ratio (DSCR):** Must be ≥1.2x for lenders

## DSCR Formula

$$DSCR = \\frac{\\text{Net Operating Cash Flow}}{\\text{Total Debt Service (P + I)}}$$
""")
    col1, col2, col3 = st.columns(3)
    with col1:
        revenue = st.number_input("Annual Revenue (₹ Cr)", value=500.0)
        opex = st.number_input("Operating Expenses (₹ Cr)", value=200.0)
    with col2:
        annual_interest_pf = st.number_input("Annual Interest (₹ Cr)", value=80.0)
        annual_principal = st.number_input("Annual Principal Repayment (₹ Cr)", value=60.0)
    with col3:
        min_dscr = st.number_input("Min DSCR Covenant", value=1.2)

    nocf = revenue - opex
    debt_service = annual_interest_pf + annual_principal
    dscr = nocf / debt_service if debt_service > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Net Operating CF", f"₹{round(nocf,2)} Cr")
    col2.metric("Total Debt Service", f"₹{round(debt_service,2)} Cr")
    col3.metric("DSCR", round(dscr,4))

    if dscr >= min_dscr:
        st.success(f"✅ DSCR {round(dscr,2)} ≥ {min_dscr} — Project can service debt")
    else:
        st.error(f"❌ DSCR {round(dscr,2)} < {min_dscr} — Insufficient cash flow for debt service!")

# =========================================================
elif menu == "Debt Restructuring & IBC 2016":
    st.header("🔄 Debt Restructuring & IBC 2016")
    st.markdown("""
## Types of Debt Restructuring

| Method | Description | When Used |
|---|---|---|
| **OTS (One-Time Settlement)** | Lender accepts partial payment to close | NPA resolution |
| **Debt Rescheduling** | Extend tenure; reduce EMI | Temporary cash flow issues |
| **Interest Rate Reduction** | Lender reduces interest rate | Distressed but viable firm |
| **Debt-to-Equity Conversion** | Lender gets equity stake | Severe distress |
| **Haircut** | Lender writes off portion of principal | Pre-IBC NPA recognition |
| **NCLT (IBC 2016)** | Formal insolvency process | When informal restructuring fails |

## Insolvency & Bankruptcy Code (IBC) 2016

**Key Provisions:**
- Time-bound resolution: **180 days** (extendable to **270 days**)
- Adjudicating authority: **NCLT** (National Company Law Tribunal)
- **Committee of Creditors (CoC):** Financial creditors drive resolution
- **Resolution Professional (RP):** Manages company during process
- **Resolution Plan:** Approved by 66% vote of CoC

## IBC Timeline
""")
    ibc_steps = [
        ("Day 1", "CIRP (Corporate Insolvency Resolution Process) begins"),
        ("Day 14", "Resolution Professional (RP) appointed"),
        ("Day 30", "Committee of Creditors (CoC) constituted"),
        ("Day 90", "Invitation for resolution plans (Expression of Interest)"),
        ("Day 180", "Resolution plan approved or liquidation ordered"),
        ("Day 270", "Final extended deadline (if approved by CoC)"),
    ]
    for day, event in ibc_steps:
        col1, col2 = st.columns([1,4])
        col1.markdown(f"**{day}**")
        col2.markdown(event)

    st.subheader("Major IBC Resolutions in India")
    ibc_cases = pd.DataFrame({
        "Company": ["Essar Steel", "Bhushan Steel", "Videocon", "DHFL", "Lanco Infratech"],
        "Debt (₹ Cr)": [54547, 56022, 90000, 87000, 46000],
        "Resolution": ["ArcelorMittal", "JSW Steel", "Vedanta", "Piramal Group", "Liquidation (partial)"],
        "Recovery %": ["92%", "~86%", "~4%", "~43%", "<5%"],
    })
    st.table(ibc_cases)

# =========================================================
elif menu == "Leverage Ratios & Credit Analysis":
    st.header("📊 Leverage Ratios & Credit Analysis")
    
    st.subheader("Key Leverage Ratios")
    col1, col2 = st.columns(2)
    with col1:
        total_debt_lr = st.number_input("Total Debt (₹ Cr)", value=2000.0)
        total_equity_lr = st.number_input("Total Equity (₹ Cr)", value=3000.0)
        ebit_lr = st.number_input("EBIT (₹ Cr)", value=500.0)
        interest_lr = st.number_input("Interest Expense (₹ Cr)", value=150.0)
    with col2:
        ebitda_lr = st.number_input("EBITDA (₹ Cr)", value=700.0)
        total_assets = st.number_input("Total Assets (₹ Cr)", value=6000.0)
        market_cap_lr = st.number_input("Market Cap (₹ Cr)", value=5000.0)

    de_ratio = total_debt_lr/total_equity_lr
    debt_to_assets = total_debt_lr/total_assets
    icr = ebit_lr/interest_lr if interest_lr > 0 else 0
    debt_ebitda = total_debt_lr/ebitda_lr if ebitda_lr > 0 else 0
    net_debt = total_debt_lr  # simplified
    net_debt_ebitda = net_debt/ebitda_lr if ebitda_lr > 0 else 0

    ratios_df = pd.DataFrame({
        "Ratio": ["D/E Ratio", "Debt/Assets", "Interest Coverage (ICR)", "Debt/EBITDA", "Net Debt/EBITDA"],
        "Formula": ["Total Debt/Total Equity", "Total Debt/Total Assets", "EBIT/Interest",
                    "Total Debt/EBITDA", "Net Debt/EBITDA"],
        "Value": [round(de_ratio,2), pct(debt_to_assets*100), round(icr,2),
                  round(debt_ebitda,2), round(net_debt_ebitda,2)],
        "Threshold (Investment Grade)": ["<1.5x", "<50%", ">3x", "<3x", "<2.5x"],
        "Status": [
            "✅" if de_ratio < 1.5 else "⚠️",
            "✅" if debt_to_assets < 0.5 else "⚠️",
            "✅" if icr > 3 else ("⚠️" if icr > 1.5 else "❌"),
            "✅" if debt_ebitda < 3 else "⚠️",
            "✅" if net_debt_ebitda < 2.5 else "⚠️",
        ]
    })
    st.dataframe(ratios_df, use_container_width=True)

# =========================================================
elif menu == "SEBI & RBI Regulations":
    st.header("⚖️ SEBI & RBI Regulations for Debt")
    
    sebi_regs = pd.DataFrame({
        "Regulation": ["SEBI (NCS) Regs 2021", "SEBI (Debenture Trustees) Regs",
                        "Min Rating", "SEBI LODR 2015", "FEMA/RBI ECB", "RBI MCLR"],
        "Key Provision": [
            "Governs issuance and listing of NCDs, CPs; replaces 2008 regulations",
            "Debenture Trustee mandatory for all public NCD issues",
            "Minimum BBB- (investment grade) for public NCD; unrated for private placement",
            "Half-yearly communication to NCD holders; stock exchange disclosure",
            "ECB framework; automatic route vs. approval route based on amount",
            "Marginal Cost of Funds-based Lending Rate — banks must link loans to MCLR"
        ]
    })
    st.table(sebi_regs)

    st.subheader("RBI Key Rates (Reference)")
    rbi_rates = {
        "Repo Rate": "6.50%",
        "Reverse Repo Rate": "3.35%",
        "CRR": "4.50%",
        "SLR": "18.00%",
        "Bank Rate": "6.75%",
        "MSF Rate": "6.75%"
    }
    cols = st.columns(len(rbi_rates))
    for i, (k, v) in enumerate(rbi_rates.items()):
        cols[i].metric(k, v)
    st.caption("Note: These are approximate rates. Check RBI website for current rates.")

# =========================================================
elif menu == "Step-by-Step Solver":
    st.header("🧠 Step-by-Step Solver")
    problem = st.selectbox("Choose Problem", [
        "Bond Price", "YTM (Approximation)", "Cost of Debt (Approx)",
        "Macaulay Duration", "DSCR", "CP Issue Price"
    ])

    if problem == "Bond Price":
        f = st.number_input("Face Value (₹)", value=1000.0)
        c_rate = st.number_input("Coupon Rate (%)", value=9.0)
        ytm_bp = st.number_input("YTM (%)", value=10.0)
        n_bp = int(st.number_input("Years", value=5, min_value=1, step=1))

        c = f * c_rate/100
        r = ytm_bp/100
        pvifa = (1-(1+r)**(-n_bp))/r
        pvif = 1/(1+r)**n_bp
        price = c*pvifa + f*pvif

        st.write("**Step 1:** Coupon = Face × Coupon Rate")
        st.latex(f"C = {f} \\times {c_rate/100} = {c}")
        st.write("**Step 2:** PVIFA and PVIF")
        st.latex(f"PVIFA = (1-{round(pvif,6)})/{r} = {round(pvifa,4)}")
        st.write("**Step 3:** Bond Price")
        st.latex(f"P = {c} \\times {round(pvifa,4)} + {f} \\times {round(pvif,6)} = {round(price,2)}")
        st.success(f"Bond Price = ₹{round(price,2)}")

    elif problem == "YTM (Approximation)":
        c = st.number_input("Annual Coupon I (₹)", value=90.0)
        fv = st.number_input("Face/Redemption Value (₹)", value=1000.0)
        p = st.number_input("Current Price (₹)", value=950.0)
        n = st.number_input("Years", value=5.0)

        num = c + (fv-p)/n
        denom = (fv+p)/2
        ytm_a = num/denom*100
        st.write("**Step 1:** Numerator = C + (F-P)/n")
        st.latex(f"= {c} + ({fv}-{p})/{n} = {round(num,4)}")
        st.write("**Step 2:** Denominator = (F+P)/2")
        st.latex(f"= ({fv}+{p})/2 = {denom}")
        st.success(f"YTM ≈ {round(num,4)}/{denom} × 100 = {round(ytm_a,4)}%")

    elif problem == "Cost of Debt (Approx)":
        I = st.number_input("Annual Interest I (₹)", value=100.0)
        RV = st.number_input("Redemption Value (₹)", value=1000.0)
        NP = st.number_input("Net Proceeds (₹)", value=960.0)
        n = st.number_input("Years", value=5.0)
        t = st.number_input("Tax Rate (%)", value=30.0)

        pre = (I+(RV-NP)/n)/((RV+NP)/2)*100
        post = pre*(1-t/100)
        st.write("**Step 1:** Kd(pre-tax)")
        st.latex(f"K_d = [{I}+({RV}-{NP})/{n}] / [({RV}+{NP})/2] \\times 100 = {round(pre,4)}\\%")
        st.success(f"Kd(after-tax) = {round(pre,4)} × (1-{t/100}) = {round(post,4)}%")

    elif problem == "Macaulay Duration":
        f = st.number_input("Face Value (₹)", value=1000.0, key="dur_f2")
        c_rate = st.number_input("Coupon Rate (%)", value=9.0, key="dur_c2")
        r = st.number_input("YTM (%)", value=10.0, key="dur_r2")/100
        n = int(st.number_input("Years", value=3, min_value=1, step=1))

        c = f*c_rate/100
        price = sum(c/(1+r)**t for t in range(1,n+1)) + f/(1+r)**n
        mac = sum(t*(c/(1+r)**t) for t in range(1,n+1))/price
        mac += n*(f/(1+r)**n)/price

        st.write("**Step 1:** Bond Price")
        st.latex(f"P = {round(price,2)}")
        st.write("**Step 2:** Macaulay Duration = Σ[t×PV(CFt)] / P")
        st.success(f"Duration = {round(mac,4)} years")
        st.success(f"Modified Duration = {round(mac/(1+r),4)}")

    elif problem == "DSCR":
        rev = st.number_input("Revenue (₹ Cr)", value=500.0)
        op = st.number_input("Operating Expenses (₹ Cr)", value=200.0)
        interest = st.number_input("Annual Interest (₹ Cr)", value=80.0)
        principal = st.number_input("Annual Principal (₹ Cr)", value=60.0)

        nocf = rev-op; ds = interest+principal; dscr = nocf/ds
        st.write("**Step 1:** NOCF = Revenue − OPEX")
        st.latex(f"NOCF = {rev} - {op} = {nocf}")
        st.write("**Step 2:** Debt Service = Interest + Principal")
        st.latex(f"DS = {interest} + {principal} = {ds}")
        st.success(f"DSCR = {nocf}/{ds} = {round(dscr,4)}")

    elif problem == "CP Issue Price":
        fv = st.number_input("Face Value (₹)", value=100000.0, key="cp_fv2")
        r = st.number_input("Discount Rate (%)", value=7.0, key="cp_r2")
        n = st.number_input("Days", value=91.0)

        ip = fv/(1+r/100*n/365)
        st.write("**Step 1:** Formula")
        st.latex(r"IP = FV / (1 + r \times n/365)")
        st.success(f"IP = {fv}/(1+{r/100}×{n}/365) = ₹{round(ip,2)}")

# =========================================================
elif menu == "AI Hint System":
    st.header("🤖 AI Hint System")
    problems_h = {
        "Bond Valuation": {
            "q": "Face=₹1000, Coupon=9%, YTM=10%, 5 years. Find bond price.",
            "correct": sum(90/(1.1)**t for t in range(1,6)) + 1000/(1.1)**5,
            "hints": ["P = C×PVIFA(r,n) + F×PVIF(r,n)",
                      "PVIFA(10%,5) = (1-1.1⁻⁵)/0.10 = 3.7908",
                      "P = 90×3.7908 + 1000×0.6209 = 341.17 + 620.92"],
            "formula": r"P = 90 \times 3.7908 + 1000 \times 0.6209 = 962.09"
        },
        "YTM Approximation": {
            "q": "Coupon=₹90, Face=₹1000, Price=₹950, 5 years. Find YTM.",
            "correct": (90+(1000-950)/5)/((1000+950)/2)*100,
            "hints": ["YTM = [C+(F-P)/n] / [(F+P)/2]",
                      "Numerator = 90 + (1000-950)/5 = 100",
                      "Denominator = (1000+950)/2 = 975"],
            "formula": r"YTM = \frac{90 + (1000-950)/5}{(1000+950)/2} = \frac{100}{975}"
        },
        "Kd After-tax": {
            "q": "Coupon=₹100, Face=₹1000, NP=₹960, 5yr, Tax=30%. Find Kd(after-tax).",
            "correct": (100+(1000-960)/5)/((1000+960)/2)*(1-0.3)*100,
            "hints": ["Kd(pre) = [100+(1000-960)/5]/[(1000+960)/2]",
                      "Numerator = 100+8 = 108, Denominator = 980",
                      "Kd(pre) = 11.02%, Kd(after) = 11.02×0.70"],
            "formula": r"K_d = \frac{108}{980} \times (1-0.30) \times 100"
        }
    }
    sel = st.selectbox("Choose Problem", list(problems_h.keys()))
    prob = problems_h[sel]
    st.markdown(f"**Problem:** {prob['q']}")
    ans = st.number_input("Your Answer", value=0.0, key="df_hint_ans")
    if st.button("Check Answer"):
        correct = prob["correct"]
        if abs(ans-correct) < abs(correct)*0.02:
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else:
            st.error(f"❌ Use hints.")
    for i, h in enumerate(prob["hints"],1):
        if st.checkbox(f"Hint {i}", key=f"dfh_{sel}_{i}"):
            st.info(f"💡 {h}")
    if st.checkbox("Show Solution", key=f"dfs_{sel}"):
        st.latex(prob["formula"])

# =========================================================
elif menu == "Quiz Engine":
    st.header("📝 Debt Financing Quiz Engine")
    difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])
    if "df_quiz_gen" not in st.session_state or st.button("🔄 New Question"):
        if difficulty == "Beginner":
            st.session_state.df_kd = random.choice([8.0,9.0,10.0,11.0])
            st.session_state.df_tax = random.choice([25.0,30.0,35.0])
            st.session_state.df_type = "kd"
        elif difficulty == "Intermediate":
            st.session_state.df_coupon = random.choice([80.0,90.0,100.0])
            st.session_state.df_fv = 1000.0
            st.session_state.df_price = random.choice([920.0,950.0,980.0])
            st.session_state.df_n = random.choice([3.0,4.0,5.0])
            st.session_state.df_type = "ytm"
        else:
            st.session_state.df_fv2 = 1000.0
            st.session_state.df_cr = random.choice([8.0,9.0,10.0])
            st.session_state.df_ytm2 = random.choice([9.0,10.0,11.0,12.0])
            st.session_state.df_n2 = random.choice([3,4,5])
            st.session_state.df_type = "bond"
        st.session_state.df_quiz_gen = True

    qtype = st.session_state.df_type
    if qtype == "kd":
        kd=st.session_state.df_kd; tax=st.session_state.df_tax
        correct=kd*(1-tax/100)
        st.markdown(f"**Find after-tax Kd:**\nPre-tax Kd={kd}%, Tax={tax}%")
    elif qtype == "ytm":
        c=st.session_state.df_coupon; fv=st.session_state.df_fv
        p=st.session_state.df_price; n=st.session_state.df_n
        correct=(c+(fv-p)/n)/((fv+p)/2)*100
        st.markdown(f"**Find YTM (approximation):**\nCoupon=₹{c}, Face=₹{fv}, Price=₹{p}, n={n}yr")
    else:
        fv=st.session_state.df_fv2; cr=st.session_state.df_cr
        ytm2=st.session_state.df_ytm2; n2=st.session_state.df_n2
        c=fv*cr/100; r=ytm2/100
        pvifa=(1-(1+r)**(-n2))/r; pvif=1/(1+r)**n2
        correct=c*pvifa+fv*pvif
        st.markdown(f"**Find Bond Price:**\nFace=₹{fv}, Coupon={cr}%, YTM={ytm2}%, n={n2}yr")

    ans=st.number_input("Your Answer",value=0.0,key="df_quiz_ans")
    if st.button("Submit"):
        if abs(ans-correct)<max(0.5,abs(correct)*0.02):
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else:
            st.error(f"❌ Answer = {round(correct,4)}")

# =========================================================
elif menu == "Excel Formula Trainer":
    st.header("📊 Excel Formula Trainer")
    problems_ex = {
        "Bond Price": {"desc":"Face=₹1000,Coupon=₹90,YTM=10%,5yr","fn":"PV","answer":"=PV(10%,5,-90,-1000)","hint":"=PV(rate,nper,-coupon,-face)"},
        "YTM Exact": {"desc":"Face=₹1000,Coupon=₹90,Price=₹950,5yr","fn":"RATE","answer":"=RATE(5,-90,950,-1000)","hint":"=RATE(nper,-coupon,price,-face)"},
        "After-tax Kd": {"desc":"Coupon=₹100,NP=₹960,Face=₹1000,5yr,Tax=30%","fn":"RATE","answer":"=RATE(5,-100,960,-1000)*(1-30%)","hint":"=RATE(...)*(1-tax)"},
        "EMI": {"desc":"Loan=₹10L,Rate=10%pa,5yr","fn":"PMT","answer":"=PMT(10%/12,60,-1000000)","hint":"=PMT(monthly_rate,months,-principal)"},
        "DSCR": {"desc":"NOCF=₹300Cr,Interest=₹80Cr,Principal=₹60Cr","fn":"=","answer":"=300/(80+60)","hint":"=NOCF/(Interest+Principal)"},
    }
    sel=st.selectbox("Choose Problem",list(problems_ex.keys()))
    prob=problems_ex[sel]
    st.markdown(f"**Problem:** {prob['desc']}")
    st.info(f"💡 Hint: `{prob['hint']}`")
    user_inp=st.text_input("Enter Excel Formula")
    if st.button("Validate"):
        if prob["fn"].upper() in user_inp.upper() or user_inp.startswith("="):
            st.success(f"✅ Reference: `{prob['answer']}`")
        else:
            st.error(f"Try using {prob['fn']}")
    if st.checkbox("Show Answer"):
        st.code(prob["answer"],language="excel")

# =========================================================
elif menu == "Formula Cheat Sheet":
    st.header("📘 Debt Financing — Formula Cheat Sheet")
    formulas = """
DEBT FINANCING — COMPLETE FORMULA REFERENCE
=============================================

BOND VALUATION
──────────────────────────────────────────────
1. Bond Price
   P = C×PVIFA(r,n) + F×PVIF(r,n)
   P = Σ[C/(1+r)^t] + F/(1+r)^n
   Excel: =PV(rate, nper, -coupon, -face)

2. PVIFA = (1-(1+r)^-n) / r
3. PVIF = 1/(1+r)^n

YIELD MEASURES
──────────────────────────────────────────────
4. Current Yield = Annual Coupon / Market Price

5. YTM (Approximation)
   YTM = [C + (F-P)/n] / [(F+P)/2] × 100
   Excel (exact): =RATE(n,-coupon,price,-face)

6. Yield to Call
   YTC = [C + (Call Price-P)/n_call] / [(Call+P)/2]

DURATION
──────────────────────────────────────────────
7. Macaulay Duration
   D_mac = Σ[t × PV(CFt)] / P

8. Modified Duration
   D_mod = D_mac / (1+r)

9. Price Change
   ΔP/P ≈ -D_mod × Δy

COST OF DEBT
──────────────────────────────────────────────
10. Simple Kd (at par)
    Kd(after-tax) = Coupon Rate × (1-t)

11. Approximation Kd
    Kd = [I+(RV-NP)/n] / [(RV+NP)/2] × 100
    Then × (1-t) for after-tax

12. YTM Method
    Excel: =RATE(n,-I,NP,-RV)×(1-t)

PROJECT FINANCE
──────────────────────────────────────────────
13. DSCR = Net Operating CF / Total Debt Service
    Debt Service = Annual Interest + Principal
    Minimum DSCR for lenders: 1.2x

COMMERCIAL PAPER
──────────────────────────────────────────────
14. CP Issue Price
    IP = FV / (1 + r × n/365)

15. CP Yield
    = (FV-IP)/IP × 365/n × 100

LEVERAGE RATIOS
──────────────────────────────────────────────
16. D/E Ratio = Total Debt / Total Equity
17. ICR = EBIT / Interest Expense
18. Debt/EBITDA = Total Debt / EBITDA
19. Net Debt/EBITDA = (Debt-Cash) / EBITDA

KEY RULES
──────────────────────────────────────────────
- Bond price ↑ when YTM ↓ (inverse relationship)
- YTM > Coupon → Discount bond (P < Face)
- YTM < Coupon → Premium bond (P > Face)
- Longer duration = more interest rate risk
- MCLR-linked loans: floating rate changes with MCLR
- ECB: add hedging cost to get INR equivalent cost
- After-tax Kd = Pre-tax Kd × (1-t) ALWAYS
=============================================
"""
    st.text_area("Formula Reference", formulas, height=700)
    st.download_button("📥 Download", data=formulas, file_name="Debt_Financing_Formulas.txt")

# =========================================================
elif menu == "Common Student Mistakes":
    st.header("⚠️ Common Student Mistakes")
    mistakes = pd.DataFrame({
        "Mistake": [
            "Using annual coupon in semi-annual bond pricing",
            "YTM approximation as exact answer",
            "Not applying (1-t) to get after-tax Kd",
            "PVIFA/PVIF calculated manually with errors",
            "Duration: using undiscounted cash flows",
            "Confusing Current Yield with YTM",
            "Bond price and yield relationship reversed",
            "ECB cost without adding hedging cost",
            "DSCR: using PAT instead of NOCF",
            "Duration of zero-coupon bond ≠ maturity",
        ],
        "Correct Approach": [
            "Semi-annual: halve coupon AND YTM; double periods: n×2",
            "YTM approx is a quick estimate. Use RATE() for exact. Approx overestimates for discounts.",
            "WACC uses after-tax Kd = Pre-tax × (1-t). Never use pre-tax in WACC.",
            "Use Excel PV/RATE/NPER functions. PVIFA = (1-(1+r)^-n)/r exactly.",
            "Duration uses PV-weighted cash flows (discounted by YTM), not raw cash flows.",
            "Current yield = coupon/price. YTM also includes capital gain/loss to maturity.",
            "Price and yield move INVERSELY. YTM rises → bond price falls. Always.",
            "ECB all-in cost = benchmark rate + spread + hedging cost. Unhedged = forex risk.",
            "DSCR = Operating Cash Flow / Debt Service. Use EBITDA-capex or FCF, not net profit.",
            "Zero-coupon bond Duration = Maturity (no intermediate cash flows — ALL at end).",
        ]
    })
    st.table(mistakes)

# =========================================================
elif menu == "Advanced Quiz Bank":
    st.header("📝 Advanced Quiz Bank")
    level = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        st.markdown("""
**Problem:** A bond: Face=₹1000, Coupon=9%, YTM=10%, 5 years annual.
(a) Find Bond Price  (b) Is it at premium, par, or discount?  (c) Why?
""")
        c=90; f=1000; r=0.10; n=5
        pvifa=(1-(1+r)**(-n))/r; pvif=1/(1+r)**n
        p=c*pvifa+f*pvif
        c1,c2=st.columns(2)
        c1.number_input("(a) Bond Price (₹)",value=0.0,step=0.01,key="aqb_beg_p")
        choice=c2.radio("(b) Bond type:",["Premium","Par","Discount"])
        reason=st.radio("(c) Why?",["YTM>Coupon","YTM=Coupon","YTM<Coupon"])
        if st.button("Evaluate",key="beg_btn"):
            a1=st.session_state.aqb_beg_p
            if abs(a1-p)<0.5 and choice=="Discount" and reason=="YTM>Coupon":
                st.success(f"✅ Price=₹{round(p,2)}, Discount (YTM>Coupon)")
                st.balloons()
            else:
                st.error(f"Price=₹{round(p,2)} | Discount bond | YTM(10%)>Coupon(9%)")

    elif level == "Intermediate":
        st.markdown("""
**Problem:** Bond: Coupon=₹90, Face=₹1000, Price=₹940, 4 years.
(a) YTM (approximation)
(b) After-tax Kd at 30% tax
(c) Current Yield
""")
        c=90;f=1000;p=940;n=4;t=30
        ytm_a=(c+(f-p)/n)/((f+p)/2)*100
        kd_at=ytm_a*(1-t/100)
        curr_y=c/p*100
        c1,c2,c3=st.columns(3)
        c1.number_input("(a) YTM %",value=0.0,step=0.01,key="aqb_int_ytm")
        c2.number_input("(b) Kd after-tax %",value=0.0,step=0.01,key="aqb_int_kd")
        c3.number_input("(c) Current Yield %",value=0.0,step=0.01,key="aqb_int_cy")
        if st.button("Evaluate",key="int_btn"):
            a1=st.session_state.aqb_int_ytm;a2=st.session_state.aqb_int_kd;a3=st.session_state.aqb_int_cy
            if all([abs(a1-ytm_a)<0.1,abs(a2-kd_at)<0.1,abs(a3-curr_y)<0.1]):
                st.success(f"✅ YTM={round(ytm_a,4)}%, Kd={round(kd_at,4)}%, CY={round(curr_y,4)}%")
                st.balloons()
            else:
                st.error(f"YTM={round(ytm_a,4)}% | Kd(at)={round(kd_at,4)}% | CY={round(curr_y,4)}%")

    elif level == "Advanced":
        st.markdown("""
**Problem:** Infrastructure project:
- Revenue=₹600Cr, OPEX=₹220Cr, Interest=₹100Cr, Principal=₹80Cr
- Bond: Face=₹1000, Coupon=9%, YTM=11%, 7 years
- Loan: ₹500Cr at 10% pre-tax, tax=25%

(a) DSCR  (b) Bond Price  (c) After-tax Kd on loan  (d) Is DSCR adequate (min 1.2x)?
""")
        nocf=600-220;ds=100+80;dscr=nocf/ds
        c=90;f=1000;r=0.11;n=7
        pvifa=(1-(1+r)**(-n))/r;pvif=1/(1+r)**n
        bp=c*pvifa+f*pvif
        kd_at=10*(1-0.25)
        c1,c2,c3,c4=st.columns(4)
        c1.number_input("(a) DSCR",value=0.0,step=0.01,key="aqb_adv_dscr")
        c2.number_input("(b) Bond Price (₹)",value=0.0,step=0.01,key="aqb_adv_bp")
        c3.number_input("(c) After-tax Kd %",value=0.0,step=0.01,key="aqb_adv_kd")
        choice=c4.radio("(d) DSCR adequate?",["Yes","No"])
        if st.button("Evaluate",key="adv_btn"):
            a1=st.session_state.aqb_adv_dscr;a2=st.session_state.aqb_adv_bp
            a3=st.session_state.aqb_adv_kd;correct_d="Yes" if dscr>=1.2 else "No"
            if all([abs(a1-dscr)<0.05,abs(a2-bp)<1,abs(a3-kd_at)<0.1,choice==correct_d]):
                st.success(f"✅ DSCR={round(dscr,2)}, Price=₹{round(bp,2)}, Kd={kd_at}%, {correct_d}")
                st.balloons()
            else:
                st.error(f"DSCR={round(dscr,2)} | Price=₹{round(bp,2)} | Kd={kd_at}% | {correct_d}")

# =========================================================
elif menu == "Progress Tracker":
    st.header("📈 Progress Tracker")
    if "df_completed" not in st.session_state: st.session_state.df_completed=[]
    if "df_scores" not in st.session_state: st.session_state.df_scores=[]
    all_modules=["Types of Debt Instruments","Term Loans & Working Capital","Bond Valuation",
                 "Yield to Maturity (YTM)","Yield Measures","Duration & Convexity",
                 "Credit Ratings","Debt Covenants","Cost of Debt (Kd)",
                 "Debt vs Equity","Secured vs Unsecured Debt","Fixed vs Floating Rate",
                 "Non-Convertible Debentures (NCDs)","Commercial Paper & T-Bills",
                 "External Commercial Borrowings (ECB)","Loan Syndication",
                 "Project Finance","Debt Restructuring & IBC 2016","Leverage Ratios & Credit Analysis"]
    selected=st.multiselect("Mark completed:",all_modules,default=st.session_state.df_completed)
    st.session_state.df_completed=selected
    col1,col2=st.columns(2)
    with col1: topic=st.selectbox("Quiz Topic",["Bond Valuation","YTM/Yield","Duration","Kd","Instruments"])
    with col2: score=st.number_input("Score (%)",0,100,75,key="df_score_inp")
    if st.button("Log Score"):
        st.session_state.df_scores.append({"topic":topic,"score":score})
        st.success("Logged!")
    n_done=len(selected);n_total=len(all_modules)
    st.metric("Modules Completed",f"{n_done}/{n_total}")
    st.progress(n_done/n_total)
    if st.session_state.df_scores:
        avg=sum(s["score"] for s in st.session_state.df_scores)/len(st.session_state.df_scores)
        st.metric("Average Score",f"{round(avg,1)}%")
    if n_done==n_total:
        st.success("🏆 All modules complete!")
        st.balloons()

# =========================================================
elif menu == "Case-Based Learning":
    st.header("📚 Case Study: Reliance Industries — Debt Strategy")
    st.markdown("""
## Background

**Reliance Industries Limited (RIL)** manages one of India's largest and most complex
debt portfolios. It demonstrates sophisticated use of multiple debt instruments.

---
## RIL Debt Profile (Approximate FY2024)

| Instrument | Amount (₹ Cr) | Rate | Tenure |
|---|---|---|---|
| Term Loans (Domestic) | ~1,20,000 | 7.5-9% | 5-15 yr |
| NCDs / Bonds | ~80,000 | 7-8.5% | 5-10 yr |
| External Commercial Borrowings | ~60,000 | SOFR+150-200bps | 5-7 yr |
| Commercial Paper | ~20,000 | 6.5-7% | 90-180 days |
| Total Debt | ~3,00,000 | Blended ~8.5% | Mix |
""")

    st.subheader("Step 1: Weighted Average Cost of Debt")
    instruments_ril = [
        ("Term Loans", 120000, 8.5, True),
        ("NCDs", 80000, 8.0, True),
        ("ECB (hedged)", 60000, 10.0, True),  # SOFR+200bps+hedging
        ("Commercial Paper", 20000, 7.0, True),
    ]
    tax_ril = 25.17
    total_d = sum(x[1] for x in instruments_ril)
    
    wacd_data = []
    for name, amt, rate, taxable in instruments_ril:
        at_rate = rate*(1-tax_ril/100) if taxable else rate
        weight = amt/total_d
        wt_cost = weight*at_rate
        wacd_data.append({"Instrument":name,"Amount (₹Cr)":amt,
                          "Pre-tax Rate":pct(rate),"After-tax Rate":pct(at_rate),
                          "Weight":pct(weight*100),"Weighted Cost":pct(wt_cost)})
    
    df_ril = pd.DataFrame(wacd_data)
    st.dataframe(df_ril, use_container_width=True)
    wacd = sum(x["Amount (₹Cr)"] * float(x["After-tax Rate"].replace("%","")) for x in wacd_data) / total_d / 100 * 100
    st.success(f"**Weighted Average Cost of Debt = {pct(wacd)}**")

    st.subheader("Step 2: Leverage Analysis")
    equity_ril = 700000  # approx RIL equity
    de_ril = total_d/equity_ril
    ebitda_ril = 180000
    icr_ril = ebitda_ril/0.085/total_d*total_d/total_d  # simplified
    debt_ebitda_ril = total_d/ebitda_ril

    col1, col2, col3 = st.columns(3)
    col1.metric("D/E Ratio", round(de_ril,2))
    col2.metric("Debt/EBITDA", round(debt_ebitda_ril,2))
    col3.metric("Total Debt", f"₹{total_d:,} Cr")

    st.subheader("Key Lessons from RIL Debt Strategy")
    lessons = [
        "**Diversified debt mix** — spreads refinancing risk across multiple instruments",
        "**ECB with hedging** — accesses cheap USD rates but must hedge forex exposure",
        "**CP for short-term** — cheaper than bank credit for working capital needs",
        "**AAA-rated** — RIL's credit rating allows access to lowest spreads",
        "**Jio/Retail separation** — subsidiaries have separate debt; ring-fenced from parent",
        "**Tax efficiency** — all interest payments generate ~25% tax shield",
    ]
    for l in lessons:
        st.markdown(f"- {l}")
