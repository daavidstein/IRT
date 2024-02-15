import streamlit as st
from dirt import irf, iic, se_est
import matplotlib.pyplot as plt
import numpy as np


with st.sidebar:
    #theta = st.slider('theta', min_value=-8.0, max_value=8.0, value=0.0)
    a = st.slider('a (Discrimination)', min_value=0.0, max_value=3.0, value=1.0)
    b = st.slider('b (Difficulty)', min_value=-8.0, max_value=8.0, value=0.0)

irf_tab, iic_tab, se_tab, var_tab, entropy_tab = st.tabs(["Item Response Function", "Item Information", "Standard Error of Estimate", "Variance", "Entropy"])

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
    disc = np.arange(0, 3, 0.6)
    fig, ax = plt.subplots()
    #for disc in np.arange(0, 3, 0.6):
    y = iic(ability=x, disc=a, diff=b,scale=False)
    ax.plot(x, y)
    plt.title(f"Item Information Function (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf"$IIC(\theta) = {a}^2 \cdot P(\theta) \cdot (1 - P(\theta))$",y = 0.85, x=0.32)
    #ax.legend(title="Discrimination")
    plt.xlabel("θ (Ability)")
    plt.ylabel("Information")
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 2.5])
    st.pyplot(fig)

with se_tab:
    x = np.arange(-4, 4, 0.1)
    disc = np.arange(0, 3, 0.6)
    fig, ax = plt.subplots()
    #for disc in np.arange(0, 3, 0.6):
    y = se_est(ability=x, disc=a, diff=b)
    ax.plot(x, y)
    plt.title(f"Standard Error of Estimate (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf'$SE_{{est}}(\theta) = \dfrac{{1}}{{\sqrt{{({a})^2 \cdot P(\theta) \cdot (1 - P(\theta))}}}}$',y = 0.23, x=0.5)
    #ax.legend(title="Discriminatioit run standn")
    plt.xlabel("θ (Ability)")
    plt.ylabel("Standard Error of Estimate")
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 5])
    st.pyplot(fig)

with var_tab:
    x = np.arange(-4, 4, 0.1)
    disc = np.arange(0, 3, 0.6)
    fig, ax = plt.subplots()
    #for disc in np.arange(0, 3, 0.6):
    prob = irf(ability=x, disc=a, diff=b)
    y = prob*(1-prob)
    ax.plot(x, y)
    plt.title(f"Item Response Variance (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf"$Var(Response(\theta)) =\cdot P(\theta) \cdot (1 - P(\theta))$", y=0.85, x=0.4)
    #ax.legend(title="Discriminatioit run standn")
    plt.xlabel("θ (Ability)")
    plt.ylabel("Variance")
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 0.3])
    st.pyplot(fig)

with entropy_tab:
    x = np.arange(-4, 4, 0.1)
    disc = np.arange(0, 3, 0.6)
    fig, ax = plt.subplots()
    #for disc in np.arange(0, 3, 0.6):
    prob = irf(ability=x, disc=a, diff=b)
    y = prob*(1-prob)
    ax.plot(x, y)
    plt.title(f"Item Response Variance (2PL) \nDifficulty={b},Discrimination={a}")
    plt.suptitle(rf"$Var(Response(\theta)) =\cdot P(\theta) \cdot (1 - P(\theta))$", y=0.85, x=0.4)
    #ax.legend(title="Discriminatioit run standn")
    plt.xlabel("θ (Ability)")
    plt.ylabel("Variance")
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 0.3])
    st.pyplot(fig)





#TODO: entropy graph
#TODO checkboxes for subplots
#TODO latex equations