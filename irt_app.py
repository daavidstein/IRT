import streamlit as st
from dirt import irf, iic, se_est
import matplotlib.pyplot as plt
import numpy as np



irf_tab, iic_tab, se_tab, var_tab, entropy_tab = st.tabs(["Item Response Function", "Item Information", "Standard Error of Estimate", "Variance", "Entropy"])


with st.sidebar:
    #theta = st.slider('theta', min_value=-8.0, max_value=8.0, value=0.0)
    a = st.slider('a (Discrimination)', min_value=0.0, max_value=3.0, value=1.0)
    b = st.slider('b (Difficulty)', min_value=-8.0, max_value=8.0, value=0.0)
    # with st.container() as ckbox_container:
    #     show_irf = st.checkbox("Item Response Function")
    #     show_iif = st.checkbox("Item Information Function")
    #     show_var = st.checkbox("Item Response Variance")
    #     show_entropy = st.checkbox("Item Entropy")
    #     show_se = st.checkbox("Standard Error of Estimation")



with irf_tab:
    x = 5
    theta = np.arange(-8.0,8.0,0.1)
    fig, ax = plt.subplots()
    plt.plot(theta,irf(ability=theta, diff =b, disc=a))
    plt.title(f"Item Response Function (2PL)"

              f"\nDifficulty={b},Discrimination={a}")
    plt.suptitle( rf'$P(\theta) = \dfrac{{1}}{{1 + e^{{-{a} \cdot (\theta - {b})}}}}$',y = 0.65, x=0.35)
    plt.xlabel("θ (Ability)")
    plt.ylabel("Probability")
    st.pyplot(fig)

with iic_tab:

    x = np.arange(-4, 4, 0.1)
    fig, ax = plt.subplots()
    y = iic(ability=x, disc=a, diff=b,scale=False)
    ax.plot(x, y)
    plt.title(f"Item Information Function (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf"$IIC(\theta) = {{{a}}}^2 \cdot P(\theta) \cdot (1 - P(\theta))$",y = 0.85, x=0.32)
    plt.xlabel("θ (Ability)")
    plt.ylabel("Information")
    ax = plt.gca()
    ax.set_ylim([0, 2.5])
    st.pyplot(fig)

with se_tab:

    x = np.arange(-4, 4, 0.1)
    fig, ax = plt.subplots()
    y = se_est(ability=x, disc=a, diff=b)
    ax.plot(x, y)
    plt.title(f"Standard Error of Estimate (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf'$SE_{{est}}(\theta) = \dfrac{{1}}{{\sqrt{{({a})^2 \cdot P(\theta) \cdot (1 - P(\theta))}}}}$',y = 0.23, x=0.5)
    plt.xlabel("θ (Ability)")
    plt.ylabel("Standard Error of Estimate")
    ax = plt.gca()
    ax.set_ylim([0, 5])
    st.pyplot(fig)

with var_tab:
    x = np.arange(-4, 4, 0.1)
    fig, ax = plt.subplots()
    prob = irf(ability=x, disc=a, diff=b)
    y = prob*(1-prob)
    ax.plot(x, y)
    plt.title(f"Item Response Variance (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf"$Var(Response(\theta)) =\cdot P(\theta) \cdot (1 - P(\theta))$", y=0.85, x=0.4)
    plt.xlabel("θ (Ability)")
    plt.ylabel("Variance")
    ax = plt.gca()
    ax.set_ylim([0, 0.3])
    st.pyplot(fig)

with entropy_tab:
    #   a = 1
    x = np.arange(-4, 4, 0.1)
    fig, ax = plt.subplots()
    prob = irf(ability=x, disc=a, diff=b)
    entropy = -sum([prob*np.log2(prob)])
    ax.plot(x, entropy)
    plt.title(f"Item Entropy (2PL)\nDifficulty={b},Discrimination={a}")
    # plt.suptitle(rf"$Var(Response(\theta)) =\cdot P(\theta) \cdot (1 - P(\theta))$", y=0.85, x=0.4)
    plt.xlabel("θ (Ability)")
    plt.ylabel("Entropy")
    ax.set_ylim([0, 0.6])
    ax = plt.gca()
    st.pyplot(fig)





#TODO: entropy graph
#TODO checkboxes for subplots
#TODO latex equations