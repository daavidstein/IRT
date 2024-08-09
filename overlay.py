import streamlit as st
from dirt import irf, iic, se_est
import matplotlib.pyplot as plt
import numpy as np



#irf_tab, iic_tab, se_tab, var_tab, entropy_tab = st.tabs(["Item Response Function", "Item Information", "Standard Error of Estimate", "Variance", "Entropy"])


with st.sidebar:
    #theta = st.slider('theta', min_value=-8.0, max_value=8.0, value=0.0)
    a = st.slider('a (Discrimination)', min_value=0.0, max_value=3.0, value=2.0)
    b = st.slider('b (Difficulty)', min_value=-8.0, max_value=8.0, value=0.0)
    # with st.container() as ckbox_container:
    #     show_irf = st.checkbox("Item Response Function")
    #     show_iif = st.checkbox("Item Information Function")
    #     show_var = st.checkbox("Item Response Variance")
    #     show_entropy = st.checkbox("Item Entropy")
    #     show_se = st.checkbox("Standard Error of Estimation")



x = np.arange(-4, 4, 0.1)
fig, ax = plt.subplots()

y = iic(ability=x, disc=a, diff=b,scale=False)
ax.plot(x, y, label="Item Information (IIF)")
plt.title(f"2PL \nDifficulty={b},Discrimination={a}")
plt.text(s=rf"$IIF(\theta) = {{{a}}}^2 \cdot P(\theta) \cdot (1 - P(\theta))$",y = 2.3, x=-4)
plt.xlabel("θ (Ability)")
#plt.ylabel("Information")
# ax = plt.gca()
# ax.set_ylim([0, 2.5])
#st.pyplot(fig)

prob = irf(ability=x, disc=a, diff=b)
y = prob*(1-prob)
ax.plot(x, y, label="Item Response Variance")
#plt.title(f"Item Response Variance (2PL) \nDifficulty={b},Discrimination={a}")
plt.text(s=rf"$Var(Response(\theta)) =\cdot P(\theta) \cdot (1 - P(\theta))$", y=2.15, x=-4)
plt.xlabel("θ (Ability)")
#plt.ylabel("Variance")
# ax = plt.gca()
# ax.set_ylim([0, 0.3])
#st.pyplot(fig)

#FIXME I think this is wrong. if the entropy is the sum over all abilities, then shouldn't it be constant
# for a given item, and not vary with ability as in our graph?
# I think maybe we want the marginal entropy - the item entropy at a given theta.
entropy = -(prob*np.log2(prob) + (1-prob)*np.log2(1-prob))
ax.plot(x, entropy,label="Item Entropy")
#plt.title(f"Item Entropy (2PL)\nDifficulty={b},Discrimination={a}")
plt.text(s=rf"$Entropy(\theta)= -[ P(\theta) \log_2(P(\theta)) + (1-P(\theta)) \log_2(1-P(\theta)) ]$", y=1.8, x=-4)
plt.xlabel("θ (Ability)")
#plt.ylabel("Entropy")
ax.set_ylim([0, 2.5])
#ax = plt.gca()
plt.legend()
plt.tight_layout()
st.pyplot(fig)





#TODO: entropy graph
#TODO checkboxes for subplots
#TODO latex equations