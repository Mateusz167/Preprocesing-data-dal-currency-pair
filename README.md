# Preprocessing of data for currency pairs
The aim of the project is to prepare the data for the currency pair for further work on them.
In the first part, 'Part 1', the programme works on real data supplied in csv format. In the second part, "Part 2", we create the data ourselves on the basis of the results of "Part 1", which are preprocessed. The assumptions are outlined below.

The actual financial data includes information on the price of the intrument and the values of the technical indicators. The decision to buy (BUY or STRONGBUY), sell (SELL or STRONGSELL), or wait (WAIT) is made based on the indicators below, as well as on the relationship between the indicators and the price. Below is a detailed description of the data:

Close - the value of the instrument at the close of a given session;
SMA14 and SMA50 - values of simple moving averages determined based on the 14 (SMA14) and 50 (SMA50) most recent readings;
SMA14IND and SMA50IND - change values for moving averages observed between adjacent readings;
Bulls - indicator indicating the strength of the bulls (the strength of the uptrend in the market).
CCI,DM, RSI - Commodity Channel Index, DeMarker and Relative
Strength Index - oscillators estimating the level of overbought (market oversold);
OSMA - Oscillator of Moving Average - moving average oscillator;
Stoch - stochastic oscillator;
Decision - value of a decision made on the basis of established values of indicators (SELL, STRONGSELL, BUY, STRONGBUY, WAIT).

The repository includes: the programme code and sample data on which actions can be performed

Part 1
    1. Load data into DataFrame format selecting only 2500 objects from the file;
    2. Remove the columns labelled SMA14IND and SMA50IND;
    3. For the Close column, count the number of occurrences of blank data. Fix the data so that the empty value is replaced by the averaged value of the two adjacent          elements;
    4. For blank data in columns SMA14 and SMA50 - fix blank values by any method;
    5. For all other attributes, fill blank values with zeros;
    6. Determine the correlation between SMA14 and SMA50;
    7. Determine correlation between Close and SMA14 and also between Close and SMA50. Remove the column for which the correlation value was greater;
    8. Provide the number of negative elements for the CCI attribute;
    9. Provide information on the maximum and minimum value for each attribute;
    10. Perform normalisation of the two selected attributes;
    11. perform a discretisation of the two selected attributes (division into 2 and 4 categories respectively);
    12. show the distribution of decision values (attribute Decision);
    13) In a line graph, show the course of the variation of the attribute Close;
    
    
Part 2
An artificial data set of the same size as the base set should be generated. At the same time, the following assumptions should be followed:

1. the first row for the data shall contain random elements in the range ⟨mini, maxi⟩, where mini is the minimum value of the i-th attribute and maxi is the maximum value of the i-th attribute;

2. the random values in the individual columns must not go outside the indicated range ⟨mini, maxi⟩, fori = 1, 2, ..., k where k is the number of attributes excluding the decision attribute;

3. the change in value for each attribute in subsequent rows must be in the range ⟨prevv al - prevv al- 1%; prevv al + prevv al- 1%⟩;

4. if the result is a value outside the max (or min) range, take the range in question as the new value;

5. once the array has been generated, count the correlation between each of the columns in the first set and the corresponding columns in the second set (i.e. the correlation between the first columns, the correlation between the second columns and so on)
