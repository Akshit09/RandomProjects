#include <SimpleModbusMaster_DUE.h>

/*
   The example will use packet1 to read a register from address 0 (the adc ch0 value)
   from the arduino slave (id=1). It will then use this value to adjust the brightness
   of an led on pin 9 using PWM.
   It will then use packet2 to write a register (its own adc ch0 value) to address 1 
   on the arduino slave (id=1) adjusting the brightness of an led on pin 9 using PWM.
*/

long previousMillis = 0;
long interval = 1000;

//////////////////// Port information ///////////////////
#define baud 9600
#define timeout 1000
#define polling 400 // the scan rate
#define retry_count 10

// used to toggle the receive/transmit pin on the driver
#define TxEnablePin 3 

#define LED 9

// The total amount of available memory on the master to store data
#define TOTAL_NO_OF_REGISTERS 3

// This is the easiest way to create new packets
// Add as many as you want. TOTAL_NO_OF_PACKETS
// is automatically updated.
enum
{
  PACKET1,
  PACKET2,
  //PACKET3,
  TOTAL_NO_OF_PACKETS // leave this last entry
};

// Create an array of Packets to be configured
Packet packets[TOTAL_NO_OF_PACKETS];

// Masters register array
unsigned int regs[TOTAL_NO_OF_REGISTERS];

void setup()
{
  Serial.begin(115200);
  Serial3.begin(baud, SERIAL_8N1);
  Serial.println("Setup()");
  // Initialize each packet
  modbus_construct(&packets[PACKET1], 7, READ_HOLDING_REGISTERS, 3030, 6, 0);
  //modbus_construct(&packets[PACKET2], 1, PRESET_MULTIPLE_REGISTERS, 1, 1, 0);
  
  //modbus_construct(&packets[PACKET1], 1, READ_INPUT_STATUS, 0, 1, 0);
  //modbus_construct(&packets[PACKET2], 1, FORCE_SINGLE_COIL, 5, 1, 1);
  //modbus_construct(&packets[PACKET3], 1, FORCE_SINGLE_COIL, 5, 1, 1);
  
  // Initialize the Modbus Finite State Machine
  modbus_configure(&Serial3, baud, timeout, polling, retry_count, TxEnablePin, packets, 1, regs);//Updated the line Total_No_of_packets = 1
  
  //pinMode(LED, OUTPUT); 
}

void loop()
{
  modbus_update();
  
  //regs[0] = analogRead(0); // update data to be written to arduino slave
  
  //analogWrite(LED, regs[0]>>2); // constrain adc value from the arduino slave to 255

  /*unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval)
  {
    previousMillis = currentMillis;
    if (regs[1] == COIL_ON)
      regs[1] = COIL_OFF;
    else
      regs[1] = COIL_ON;
  }*/
 delay(5000);
  /*
  if (regs[0] & 0x0001 == 1)
    regs[1] = COIL_ON;
  else
    regs[1] = COIL_OFF;*/
}
