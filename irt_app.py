import streamlit as st
from dirt import irf, iic, se_est
import matplotlib.pyplot as plt
import numpy as np
with st.sidebar:
    #theta = st.slider('theta', min_value=-8.0, max_value=8.0, value=0.0)
    a = st.slider('a (Discrimination)', min_value=0.0, max_value=3.0, value=1.0)
    b = st.slider('b (Difficulty)', min_value=-8.0, max_value=8.0, value=0.0)

irf_tab, iic_tab, se_tab = st.tabs(["Item Response Function", "Item Information", "Standard Error of Estimate"])
with irf_tab:
    theta = np.arange(-8.0,8.0,0.1)
    fig, ax = plt.subplots()
    plt.plot(theta,irf(ability=theta, diff =b, disc=a))
    plt.title(f"Item Response Function  (2PL)\nDifficulty={b},Discrimination={a}")
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
    #ax.legend(title="Discrimination")
    plt.xlabel("θ (Ability)")
    plt.ylabel("Standard Error of Estimate")
    ax = plt.gca()
    #ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 2.5])
    st.pyplot(fig)

