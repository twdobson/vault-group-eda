# Nic Notes

- File 'type_1_duressed_unit_data.pkl' has 'types' 0,1,2,3 thousand; where 6000 is the 'duress' code? 
- File 'samples.pickle' contains the values: ['type', 'log_level', 'facility']
- 

## LOG KEYS

- (success, type, log_level, facility, unit_id, capture_time, receive_time, data) - Type 1: 14,734,750
- (datetime, user, level, facility, data) - Type 2: 3,671,088



## Type 2:
- Columns:  ['datetime', 'user', 'level', 'facility', 'data']
- Type 2:
- Level: E,I,W -> what are these? 


## Type 1:
- Columns:  ['success', 'type', 'log_level', 'facility', 'unit_id', 'capture_time','receive_time', 'data']
- in Type 1: Data column has 'Locked[1...21]
- What is 'duress threshold' ("Message validation failed for settings read from server: Invalid duress threshold")
- Unlock message? (unlock(): Unlocking 0:1 failed ) - what is the ratio of numbers
- 'Time at which units locked' Graph indicates most vaults locked at around 5:30am to 7:00pm (service the machines between these times)

## Unit cv730
### Common Error messages 
- 'Error retrieving server time: null'   
- 'Error setting system time from RTC: Invalid date 'NOVEMBER 31'  
- 'Error sending status to server: null'
- 'Lost protocol synchronization with master board'
- 'Error retrieving upgrade version data'
- 'Error retrieving new settings.  null response (network error?)'
- 'Error setting system date and time'
- 'Error pinging slave: 3. msg is null. errorCount==2'

#### Board Structure
- 'Slave health (RS485) [Tot/Suc/Err/%Err]: [1692/1692/0/0.00%],[1692/1692/0/0.00%],[1692/1692/0/0.00%],[1692/1692/0/0.00%],[1692/1692/0/0.00%]'
- From the above we can assume there are 5 slaves, so therefore 5 columns
- can only see 26 lockers (highest number in the log data snippet I can see)
- Locker state on slave 2 changed from [S]-L-U-L-L-L-L-[E] to [S]-L-L-L-L-L-L-[E]
- Can pull number of lockers and start locker states from these messages
- Slave 0: 5 lockers
- Slave 1: 6 lockers
- Slave 2: 6 lockers
- Slave 3: 6 lockers
- Slave 4: 3 lockers

