#include <iostream> //include the iostream file for iostreams to function properly
#include <string> //include the string header to utilize the string data type
using namespace std; //use the standard namespace for ease of coding output and input streams

//***GLOBAL VALUES***
#define COFFEE_PRICE 0.75
#define DECAF_PRICE 0.75
#define SUGAR_PRICE 0.25
#define CREAM_PRICE 0.25
#define SMILK_PRICE 0.35
#define FMILK_PRICE 0.35
#define ESPRESSO_PRICE  1.10
#define COCOA_PRICE  0.90
#define WHIPPED_PRICE  1.00
#define COFFEE  10
#define DECAF  10
#define SUGAR  10
#define CREAM  10
#define SMILK  10
#define CFMILK  10
#define ESPRESSO  10
#define COCOA  10
#define WHIPPED  10

//check_status method (works; not being used currently)
string check_status(int a, int b=1, int c=1, int d=1)
{
	string m_status_return = "Available"; //set the status to true by default
	
	if (a <= 0)
	{
		m_status_return = "Unavailable"; //if the inventory for a is 0 or less, return false
	}
	
	if (b <= 0)
	{
		m_status_return = "Unavailable"; //if the inventory for b is 0 or less, return false
	}
	
	if (c <= 0)
	{
		m_status_return = "Unavailable"; //if the inventory for c is 0 or less, return false
	}
	if (d <= 0)
	{
		m_status_return = "Unavailable"; //if the inventory for d is 0 or less, return false
	}
		
	return m_status_return;  //return the status to main	
}
void display_checkedmenu(int &dci_coffee, int &dci_decaf, int &dci_sugar, int &dci_cream, int &dci_smilk, int &dci_fmilk, int &dci_espresso, int &dci_cocoa, int &dci_whipped)
{
	//decalre local function variables
	string americano_status = "Available";
	string latte_status = "Available";
	string mocha_status = "Available";
	string cappucinno_status = "Available";
	string coffee_status = "Available";
	string decaf_status = "Available";

	//check for unavailable drinks
	//check coffee inventory
	if((dci_coffee < 3) || (dci_sugar < 1) || (dci_cream < 1)){coffee_status = "Unavailable";}

	//check decaf inventory
	if((dci_decaf < 3) || (dci_sugar < 1) || (dci_cream < 1)){decaf_status = "Unavailable";}

	//check caffe latte inventory
	if((dci_espresso < 2) || (dci_smilk < 1)){latte_status = "Unavailable";}

	//check caffe americano inventory
	if((dci_espresso < 3)){americano_status = "Unavailable";}

	//check caffe mocha inventory
	if((dci_espresso < 1) || (dci_cocoa < 1) || (dci_smilk < 1) || (dci_whipped < 1)){mocha_status = "Unavailable";}

	//check cappuccino inventory
	if((dci_espresso < 2) || (dci_smilk < 1) || (dci_fmilk < 1)){cappucinno_status = "Unavailable";}

	//display menu
	cout << "Current Menu:\n";
	cout << "-------------\n\n";
	cout << "1,Caffe Americano,$" << (3*ESPRESSO_PRICE) << "," << americano_status << "\n\n";
	cout << "2,Caffe Latte,$" << (2*ESPRESSO_PRICE+SMILK_PRICE) << "," << latte_status << "\n\n";
	cout << "3,Caffe Mocha,$" << (ESPRESSO_PRICE+COCOA_PRICE+SMILK_PRICE+WHIPPED_PRICE) << "," << mocha_status << "\n\n";
	cout << "4,Cappuccino,$" << (2*ESPRESSO_PRICE+SMILK_PRICE+FMILK_PRICE) << "," << cappucinno_status << "\n\n";
	cout << "5,Coffee,$" << (3*COFFEE_PRICE+SUGAR_PRICE+CREAM_PRICE) << "," << coffee_status << "\n\n";
	cout << "6,Decaf Coffee,$" << (3*DECAF_PRICE+SUGAR_PRICE+CREAM_PRICE) << "," << decaf_status << "\n\n";
	cout << "\n\n";
	cout << "Please make a selection from the above menu (using values 1 - 6)\n";
	cout << "Alternately press Q to quit the menu, or press R to reload the menu and inventory\n";

	 //return nothing to main but the output
}

//make a cup of Caffe Americano (working)
void make_CaffeAmericano(int &mca_a)
{
	//check for negative inventory
	if ((mca_a - 3) > 0) 
	{(mca_a = mca_a-3);} //remove used inventory
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}
}

//make a cup of Caffe Latte (working)
void make_CaffeLatte(int &mcl_a,int &mcl_b)
{
	//check for negative inventory
	if (((mcl_a - 2) >= 0) && ((mcl_b - 1) > 0))
	{
		//remove used inventory
		mcl_a = mcl_a-2;
		mcl_b--;
	}
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}
}

//make a cup of Caffe Mocha (working)
void make_CaffeMocha(int &mcm_a,int &mcm_b,int &mcm_c,int &mcm_d)
{
	//check for negative inventories
	if(((mcm_a - 1) >= 0) && ((mcm_b - 1) >= 0) && ((mcm_c - 1) >= 0) && ((mcm_d - 1) >= 0))
	{
		//remove used inventory
		mcm_a--;
		mcm_b--;
		mcm_c--;
		mcm_d--;
	}
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}

}

//make a cup of Cappuccino (working)
void make_Cappuccino(int &mcap_a,int &mcap_b,int &mcap_c)
{
	//check for negative inventories
	if(((mcap_a - 2) >= 0) && ((mcap_b - 1) >= 0) && ((mcap_c - 1) >= 0))
	{
		//remove used inventory
		mcap_a = mcap_a - 2;
		mcap_b--;
		mcap_c--;
	}
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}
}

//make a cup of Coffee (working)
void make_Coffee(int &mcof_a,int &mcof_b,int &mcof_c)
{
	//check for negative inventories
	if(((mcof_a - 3) >= 0) && ((mcof_b - 1) >= 0) && ((mcof_c - 1) >= 0))
	{
		//remove used inventory
		mcof_a = mcof_a - 3;
		mcof_b--;
		mcof_c--;
	}
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}
}

//make a cup of Decaf (working)
void make_Decaf(int &md_a,int &md_b,int &md_c)
{
	//check for negative inventories
	if(((md_a - 3) >= 0) && ((md_b - 1) >= 0) && ((md_c - 1) >= 0))
	{
		//remove used inventory
		md_a = md_a - 3;
		md_b--;
		md_c--;
	}
	else
	{
		cout << "The selected drink is unavailable at this time, please choose a different menu item.\n\n";
	}
}

void display_errormessage(char input_error)
{
	cout << "\n\nThe selection you made of " << input_error << " is an invalid menu choice. Please try again with a valid choice...";
}