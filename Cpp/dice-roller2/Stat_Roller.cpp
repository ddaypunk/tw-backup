// Stat_Roller.cpp : main project file.

#include "stdafx.h"

using namespace std;

int main()
{
	char choice = 'm';
	int die1, die2, die3, die4;
	int roll_array[6];
	srand ( (unsigned)time(0) ); //set the seed to the system clock value

	while(choice == 'm')
	{
	//roll 4d6 and add them together
	//add functionality to drop the lowest and then add
    for(int i = 0; i < 6; i++)
	{
		die1 = ((rand() % 6) +1); //generate 4 die rolls between 1 and 6
		die2 = ((rand() % 6) +1);
		die3 = ((rand() % 6) +1);
		die4 = ((rand() % 6) +1);

		if ((die1 < die2) && (die1 < die3) && (die1 < die4))
		{ 
			roll_array[i] = (die2 + die3 + die4);
		}

		if ((die2 < die1) && (die2 < die3) && (die2 < die4))
		{ 
			roll_array[i] = (die1 + die3 +die4);
		}

		if ((die3 < die1) && (die3 < die2) && (die3 < die4))
		{ 
			roll_array[i] = (die1 + die2 + die4);
		}

		if ((die4 < die1) && (die4 < die2) && (die4 < die3))
		{ 
			roll_array[i] = (die1 + die2 + die3);
		}

		cout << "Roll " << i+1 << ": " << roll_array[i] << "\n\n";
		
	}
	cout << "If you would like to take a Mulligan and re-roll, please press \"m\"...\n";
	cin >> choice;
	}//endwhile
    return 0;
}
