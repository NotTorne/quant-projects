import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


# input the long moving average and short moving average period
# for the classic MACD, it is 12 and 26
# once a upon a time you got six trading days in a week
# so it is two week moving average versus one month moving average
# for now, the ideal choice would be 10 and 21

#simple moving average
def macd(signals):
    signals['mov_avg1'] = signals['Close'].rolling(window = mov_avg1, min_periods = 1, center = False).mean()
    signals['mov_avg2'] = signals['Close'].rolling(window = mov_avg2, min_periods = 1, center = False).mean()

    return signals

#signal generation
#when the short moving average is larger than long moving average, we long and hold
#when the short moving average is smaller than long moving average, we clear positions
#the logic behind this is that the momentum has more impact on short moving average
#we can subtract short moving average from long moving average
#the difference between is sometimes positive, it sometimes becomes negative
#thats why it is named as moving average converge/diverge oscillator

def generate_signal(df, method):

    signals = method(df)
    signals['positions'] = 0

    #positions becomes and stays one once the short moving average is above long moving average
    signals['positions'][mov_avg1:] = np.where(signals['mov_avg1'][mov_avg1:]>=signals["mov_avg2"][mov_avg1:], 1, 0)

    #as positions only imply the holding
    #we take the difference to generate real trade signal
    signals['signals'] = signals['positions'].diff()

    #oscillator is the difference between two moving average
    #when it is positive, we long, vice versa
    signals['oscillator'] = signals['mov_avg1']-signals['mov_avg2']

    return signals



#plotting the backtesting result
# def plot(new, ticker):
    
#     #the first plot is the actual close price with long/short positions
#     fig=plt.figure()
#     ax=fig.add_subplot(111)
    
#     new['Close'].plot(label=ticker)
#     ax.plot(new.loc[new['signals']==1].index,new['Close'][new['signals']==1],label='LONG',lw=0,marker='^',c='g')
#     ax.plot(new.loc[new['signals']==-1].index,new['Close'][new['signals']==-1],label='SHORT',lw=0,marker='v',c='r')

#     plt.legend(loc='best')
#     plt.grid(True)
#     plt.title('Positions')
    
#     plt.show()
    
#     #the second plot is long/short moving average with oscillator
#     #note that i use bar chart for oscillator
#     fig=plt.figure()
#     cx=fig.add_subplot(211)

#     new['oscillator'].plot(kind='bar',color='r')

#     plt.legend(loc='best')
#     plt.grid(True)
#     plt.xticks([])
#     plt.xlabel('')
#     plt.title('MACD Oscillator')

#     bx=fig.add_subplot(212)

#     new['mov_avg1'].plot(label='mov_avg1')
#     new['mov_avg2'].plot(label='mov_avg2',linestyle=':')
    
#     plt.legend(loc='best')
#     plt.grid(True)
#     plt.show()

def plot(new, ticker):
    # First plot: Actual close price with long/short positions
    fig1 = plt.figure()
    ax = fig1.add_subplot(111)
    
    new['Close'].plot(label=ticker)
    ax.plot(new.loc[new['signals'] == 1].index, new['Close'][new['signals'] == 1], 
            label='LONG', lw=0, marker='^', c='g')
    ax.plot(new.loc[new['signals'] == -1].index, new['Close'][new['signals'] == -1], 
            label='SHORT', lw=0, marker='v', c='r')
    
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Positions')
    plt.show()
    
    # Second set of plots: Oscillator and moving averages
    fig2 = plt.figure()
    
    # Subplot 1: MACD Oscillator
    cx = fig2.add_subplot(211)
    new['oscillator'].plot(kind='bar', color='r')
    plt.legend(['Oscillator'], loc='best')
    plt.grid(True)
    plt.xticks([])
    plt.title('MACD Oscillator')
    
    # Subplot 2: Moving Averages
    bx = fig2.add_subplot(212)
    new['ma1'].plot(label='ma1')
    new['ma2'].plot(label='ma2', linestyle=':')
    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Moving Averages')
    
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


def main():
    global mov_avg1, mov_avg2, st_date, end_date, ticker, slicer
    #macd is easy and effective
    #there is just one issue
    #entry signal is always late
    #watch out for downward EMA spirals!

    # mov_avg1 = int(input("Enter moving average 1 period: "))
    # mov_avg2 = int(input("Enter moving average 2 period: "))
    # st_date =  input("Enter start date in format yyyy-mm-dd: ")
    # end_date = input("Enter end date in format yyyy-mm-dd: ")
    # ticker = input("Enter ticker: ")
    mov_avg1 = 12
    mov_avg2 = 26
    st_date = '2010-01-01'
    end_date = '2020-01-01'
    ticker = 'AAPL'
    # slicer = 16
    
    #slicing the downloaded dataset
    #if the dataset is too large, backtesting plot would look messy
    #you get too many markers cluster together
    # slicer=int(input('slicing:'))

    df = yf.download(ticker, start = st_date, end = end_date)    
    new = generate_signal(df, macd)
    plot(new, ticker)
if __name__ == '__main__':
    main()

       