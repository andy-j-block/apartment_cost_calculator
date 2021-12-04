import streamlit as st

GROSS_MONTHLY: int
LEASE_LENGTH: float
CONCESSIONS: bool
MONTHS_OFF: float
BROKERS_FEE: bool
PERCENTAGE: float

def calculate_net_monthly(gross_monthly, lease_length, concessions, months_off, brokers_fee, percentage):
    net_total = gross_monthly*lease_length

    if concessions: net_total -= gross_monthly*months_off
    if brokers_fee: net_total += gross_monthly*12*(percentage/100)

    return net_total/lease_length

header = st.container()
init_terms_container = st.container()
concessions_container = st.container()
brokers_fee_container = st.container()
net_cost_container = st.container()

with header:
    st.title('Apartment Cost Calculator')
    st.write("""
        This app computes the net cost of renting an apartment in NY.  Required are the gross cost per month and
        lease length.  Optional inputs are any concessions and/or broker's fees involved in the rental.
        """)
    st.write('')

with init_terms_container:
    gross_monthly_input, lease_length_input = st.columns(2)
    GROSS_MONTHLY = int(gross_monthly_input.text_input(label='Gross Monthly Cost:', value='0'))
    LEASE_LENGTH = lease_length_input.number_input('Lease length:', value=12.0, step=0.5, format='%f')

with concessions_container:
    concession_toggle, months_off_input = st.columns(2)
    concession_bool = concession_toggle.radio('Concessions?', ('No', 'Yes'))
    concession_toggle.write('<style>div.row-widget.stRadio > div{flex-direction:row; float:left; padding: 5px;}</style>', unsafe_allow_html=True)
    CONCESSIONS = True if concession_bool == 'Yes' else False

    MONTHS_OFF = months_off_input.number_input('Months off:', min_value=0.0, step=0.25, format='%f')

with brokers_fee_container:
    brokers_fee_toggle, percentage_input = st.columns(2)
    brokers_fee_bool = brokers_fee_toggle.radio('Brokers Fee?', ('No', 'Yes'))
    BROKERS_FEE = True if brokers_fee_bool == 'Yes' else False

    PERCENTAGE = percentage_input.number_input('Percentage:', value=0.0, step=0.5, format='%f')

with net_cost_container:
    net_monthly = calculate_net_monthly(GROSS_MONTHLY, LEASE_LENGTH, CONCESSIONS, MONTHS_OFF, BROKERS_FEE, PERCENTAGE)
    st.subheader('Net monthly cost is:')
    st.write(f'${net_monthly:0.2f}')