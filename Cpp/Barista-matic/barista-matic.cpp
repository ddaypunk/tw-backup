#include "barista_extras.h" //include the header that includes the globals and functions
//***MAIN START***
int main ()
{
char selection = '0'; //set menu selection to a default value of running the application
double coffee_price = COFFEE_PRICE;  //not sure these declarations really matter as this would
double decaf_price = DECAF_PRICE;    //cause them to reset each time the loop runs
double sugar_price = SUGAR_PRICE;    //might need to use these in the Reset and display routine
double cream_price = CREAM_PRICE;
double smilk_price = SMILK_PRICE;
double fmilk_price = FMILK_PRICE;
double espresso_price = ESPRESSO_PRICE;
double cocoa_price = COCOA_PRICE;
double whipped_price = WHIPPED_PRICE;

int coffee = COFFEE;
int decaf= DECAF;
int sugar = SUGAR;
int cream = CREAM;
int smilk = SMILK;
int fmilk = CFMILK;
int espresso = ESPRESSO;
int cocoa = COCOA;
int whipped = WHIPPED;

while((selection != 'q') || (selection != 'Q'))        //run the menu as long as the quit command is not encountered                         
{
	//display program title
	cout << "*==============================*\n";
	cout << "|Welcome to Barista-Matic:     |\n";
	cout << "|Your daily dose of caffeine!!!|\n";
	cout << "*==============================*\n\n";

	//display inventory
	cout << "Current Inventory: \n";
	cout << "------------------\n\n";
	cout << "Cocoa," << cocoa << "\n\n"; 
	cout << "Coffee," << coffee << "\n\n";
	cout << "Cream," << cream << "\n\n"; 
	cout << "Decaf Coffee," << decaf << "\n\n"; 
	cout << "Espresso," << espresso << "\n\n"; 
	cout << "Foamed Milk," << fmilk << "\n\n"; 
	cout << "Steamed Milk," << smilk << "\n\n"; 
	cout << "Sugar," << sugar << "\n\n"; 
	cout << "Whipped Cream," << whipped << "\n\n";

	//display the menu with inventory checks
	display_checkedmenu(coffee,decaf,sugar,cream,smilk,fmilk,espresso,cocoa,whipped);

	//ask for menu selection
	cin >> selection;
	//determine routine based on selection (switch statement) and run selected routine
	if (selection == '1'){make_CaffeAmericano(espresso);}
	if (selection == '2'){make_CaffeLatte(espresso,smilk);}
	if (selection == '3'){make_CaffeMocha(espresso,cocoa,smilk,whipped);}
	if (selection == '4'){make_Cappuccino(espresso,smilk,fmilk);}
	if (selection == '5'){make_Coffee(coffee,sugar,cream);}
	if (selection == '6'){make_Decaf(decaf,sugar,cream);}
	if ((selection != 'q') && (selection != 'Q') &&(selection != 'r') && (selection != 'R') && (selection != '1') && (selection != '2') && (selection != '3') && (selection != '4') && (selection != '5') && (selection != '6'))
	{display_errormessage(selection);}


	//selected routine will also display the output
	//ex. 
	//backup if to exit the loop as the loop is not working
	if ((selection == 'Q') || (selection == 'q'))
		{ 
			cout << "Thank you for choosing Barista-Matic for all your caffeine needs...\n\n";
			system("PAUSE");
			break; 
		}
	if ((selection == 'R') || (selection == 'r'))
		{ 
			coffee = COFFEE;
			decaf= DECAF;
			sugar = SUGAR;
			cream = CREAM;
			smilk = SMILK;
			fmilk = CFMILK;
			espresso = ESPRESSO;
			cocoa = COCOA;
			whipped = WHIPPED; 
		}
} //end of the do while statement
 return 0;
} //End of main
//***END MAIN***

//idea: create a class Drink that will have a spot for up to 4 ingredients for passing to functions?