from digital_data_to_signal import dataToSignal
from gui import gui


if __name__ == '__main__':

    data = dataToSignal('101000110')

    # Print converted signals
    print("NRZ Signal:", data.NRZ())
    print("NRZI Signal:", data.NRZI())
    print("Manchester Signal (IEEE 802.3 compliant):", data.toManchester(ieee802dot3=True))
    print("Differential Manchester Signal:", data.toDifferentailManchester())


    # visualising signals using matplotlib
    g = gui(mybin=data)

    g.plot_NRZL()
    g.plot_NRZI()
    g.plot_Manchester()
    g.plot_DifferentailManchester()
