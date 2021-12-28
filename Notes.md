# Tim's vault group data notes

### Data summary

Raw log data
- There are two formats of data present in the log files:
  - Type 1 has columns: 'success', 'type', 'log_level', 'facility', 'unit_id', 'capture_time', 'receive_time', 'data'
  - Type 2 has columns: 'datetime', 'user', 'level', 'facility', 'data'
- Type 1 represents 80% of rows (14,734,751), type 2 represents 20% of the rows (3,671,089)
- However, 95% of type 2 data is for a dummy user. Therefore, there are 211,699 potentially valid rows


Type 2 data
- There are 1726 users in the data
- However, removing duplication caused by 'unit ' prefix we get 1282 units (~25% reduction)
- User field contains None, why is this missing?
- There are names and other unexpected values:  bongani, faeem, lindiwe, florence, james, abbie, lindi, lance, sameena, gerhard, alois, darryn, alicia, vitaliy, vitaly, adaan, mariusv, nicholas, leon, sanele, juan, mario, Michael, mike, neil, sihle, 647378, larryl, pierre, Mario, vitalii, nobody'

### Field summary

Type 2 data (based on sample data)
- **type**:
  - 0: appears to be related to server + unit communications
  - 1000: Related to locker release timer
  - 2000: Locker status + locker release time
  - 3000: relates to lockers unlocking, including adding to queues, updating release timing
  - 6000: Duress detected
- **log level**
  - I: General information
  - E: Usually server communications error
  - F: Failure? Appears to be 'Lost protocol synchronization with master board' (Facility = master)
  - W: Withdrawal issue related? Includes 'error: queue full' or unable to unlock locker (Facility = MSM)
  - D: Config related? Data includes machine state information messages (Facility = Config)
- **Facility**
  - SM: Slave communications including slave health (Log level = I / E)
  - SrvrComms: Messages between server and ... ? Mostly Information requests (time, upgrade info, status) unless it is an error (log level = I / E)
  - Master: Seems equivalent to log level F = 'Lost protocol synchronization with master board'
  - UnitMain: Relates to system date and time setting / synicing (log level = only error)
  - Service: Service related information? 'Started audit', 'Started SM', 'Started MSM', 'MSM caught must die flag' (log level = I)
  - Main: Unit start up and unit switch off (log level = I)
  - StngsMng: Relates to Settings. All data is 'Settings read successfully' (log level = I)
  - MqttManager: All data is 'No default unit settings available. Waiting'
  - MSM: Data is either 'Entering full lockdown' or successful queue related (Log level = I)
  - AdminPwModule: Only data is 'Invalid admin password specified'
  - Utils: Error messages, usually relating to versions of things not found
  - UnitSettingUtils: Error messages, only data is 'Error reading config message'
  - UnitSettingsUtils: Info messages, either 'UnitSettingsUtils lock engaged' or actual config data is json format.
  - UnitSettingMsg: Info relating to settings being saved / new settings
  - Config: Either info messages on config changes or flag setting for starting main machine
  - OVPNMon: Info messages relating to openvpn monitoring
  - SysMon: Info relating to System monitoring starting
  - SSHMon: Info message, data is only 'No tunnel detected. Shutting down SSH'
  - AdminSM: Relates to admin settings being managed
  - InstallSM: Relates to machine startup and registration



##  Data issues
Type 2 data
- User type 'none'
- word 'unit' followed by valid unit name (for facility = unitmanager_pingUnit)
- 





## Other data potentially available?
- Servicing history
- Lookup tables of any kind?
- Unit information? E.g. how many lockers per unit
- Error ID
    - type + log level + facility does not give granular view of data
    - However, data field is too specific


## Potential investigations
- Unit utilisation: e.g. 50% of lockers are used
  - need to know how many lockers per Unit
- Lockers needed
  - Size of locker used
  - Mixed of lockers best suited to client
- Proactive additional sales
  - Increasing utilisation nearing 100% utilisation =>  engage client

