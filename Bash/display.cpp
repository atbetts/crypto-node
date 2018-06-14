#include <stdio.h>
#include "upm/lcm1602.hpp"
#include <iostream>
#include <string>
#define I2C_BUS 0
using namespace std;

int main (int argc, char* argv[]){
	upm::Lcm1602 lcd(I2C_BUS,0x27,true,20,4);
	lcd.autoscrollOff();
	string word = argv[1];
	cout<< word.length() << endl;
	lcd.setCursor(0,0);
	uint8_t j = 0;
	for(uint8_t i =0; i< word.length();i++){
		if(i>=80&&j<4){
			break;
		}
		else if(i>=60 && j<3){
			lcd.setCursor(3,0);
			j++;
		}
		else if(i>=40 && j<2){
			lcd.setCursor(2,0);
			j++;
		}
		else if(i>=20 && j<1){
			lcd.setCursor(1,0);
			j++;
		}

		lcd.write(string(1,*(argv[1]+i)));
	}
	return 0;

}
