import streamlit as st

GROSS_MONTHLY: int
LEASE_LENGTH: float = 12.0
CONCESSIONS: bool = False
MONTHS_OFF: float = 0.0
BROKERS_FEE: bool = False
PERCENTAGE: float = 0.0

def calculate_net_monthly(GROSS_MONTHLY, LEASE_LENGTH, CONCESSIONS, MONTHS_OFF, BROKERS_FEE, PERCENTAGE):
    net_monthly = GROSS_MONTHLY

    if CONCESSIONS:
        net_monthly = GROSS_MONTHLY*(LEASE_LENGTH-MONTHS_OFF)/LEASE_LENGTH

    # if BROKERS_FEE:
    #     net_monthly

    return net_monthly

header = st.container()
init_terms_container = st.container()
concessions_container = st.container()
brokers_fee_container = st.container()
net_cost_container = st.container()

with header:
    st.title('Apartment Cost Calculator')
    st.write("""
        This app computes the net cost of renting an apartment in NY.  Required are the gross cost per month and any
        concessions and/or broker's fee involving in the rental.
        """)
    st.write('')

with init_terms_container:
    gross_monthly_input, lease_length_input = st.columns(2)
    GROSS_MONTHLY = int(gross_monthly_input.text_input(label='Gross Monthly Cost:', value='0'))
    LEASE_LENGTH = lease_length_input.number_input('Lease length:', value=12.0, step=0.5, format='%f')

with concessions_container:
    concession_toggle, months_off_input = st.columns(2)
    concession_bool = concession_toggle.radio('Concessions?', ('No', 'Yes'))
    if concession_bool == 'Yes': CONCESSIONS is True

    MONTHS_OFF = months_off_input.number_input('Months off:', min_value=0.0, step=0.25, format='%f')

with brokers_fee_container:
    brokers_fee_toggle, percentage_input = st.columns(2)
    brokers_fee_bool = brokers_fee_toggle.radio('Brokers Fee?', ('No', 'Yes'))
    if brokers_fee_bool == 'YES': BROKERS_FEE is True

    PERCENTAGE = percentage_input.number_input('Percentage:', value=0.0, step=0.5, format='%f')

with net_cost_container:
    calculate_net_monthly(GROSS_MONTHLY, LEASE_LENGTH, CONCESSIONS, MONTHS_OFF, BROKERS_FEE, PERCENTAGE)
