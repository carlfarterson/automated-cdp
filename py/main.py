import pandas as pd
from py.cdp import CDP


def main():

    df = pd.DataFrame(columns=['non_CDP', 'CDP_1', 'CDP_2'])
    cdp_1 = CDP()
    withdrawal_1 = cdp_1.usd_available_to_generate * 0.5
    cdp_1.generate_usd(withdrawal_1)
    cdp_1.deposit_eth(eth=withdrawal_1/cdp_1.price)
    cdp_2 = cdp_1
    withdrawal_2 = cdp_2.usd_available_to_generate * 0.5
    cdp_2.generate_usd(withdrawal_2)
    cdp_2.deposit_eth(eth=withdrawal_2/cdp_2.price)

    for i in range(100, 1000):
        non_CDP = i
        CDP_1 = cdp_1.close(price=i) * i
        CDP_2 = cdp_2.close(price=i) * i
        df.append([non_CDP, CDP_1, CDP_2], ignore_index=True)

    df.to_csv('data/cdp_comparison.csv')


if __name__ == '__main__':
    main()
