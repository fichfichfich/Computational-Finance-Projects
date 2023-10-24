#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 2 Part 3: Bonds and Bond Math
 Bond Auction
 
 https://cs-people.bu.edu/azs/fe459/assignments/a2.html
 
 a2task3.py
"""

from a2task1 import *

def collect_bids(filename):
    """
    To process the data file containing the bids.
    """
    
    # Open file
    file = open('bond_bids.csv', 'r')
    
    # Empty list
    bid_list = []
    
    # Loop for reading the CSV File
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        bid_id = fields[0]
        bid_amount = fields[1]
        bid_price = fields[2]
        
        # Removes header
        if (bid_id == 'bid_id'):
            list1 = []
        
        # Everything else (bids) get added to the list
        else:
            list1 = [int(bid_id), int(bid_amount), float(bid_price)]
            bid_list.append(list1)
        
    # Returns the list
    return bid_list



def print_bids(bids):
    """
    Process the a of bids, and produce a beautifully-formatted table of the bids. 
    """

    # Headers
    print(f"{'Bid ID':<13}{'Bid Amount':<14}{'Price':<7}")
    
    # Loop for bid_id, bid_amount, bid_price
    for bid in bids:
        bid_id, bid_amount, bid_price = bid
        
        # Format and print
        print(f"{bid_id:>6}{f'${bid_amount:>9}':>17}{f'${bid_price:>10,.3f}':>15}")
        
### Testing
#bids = collect_bids('./bond_bids.csv')
#print_bids(bids)
    
    
    
def find_winning_bids(bids, total_offering_fv, c, n, m):
    """
    Processes a list of bids and determine which are successful in the auction. 
    
    The parameters are:
        bids, where each bid is a sublist in the form of [bid_id, bid_amount, bid_price],
        total_offering_fv is the total amount of bonds being sold,
        c is the annualized coupon rate,
        n is the number of years to maturity for the bonds, and
        m is the number of coupon payments per year.
    """
    
    # Sort List in order of bids
    print ("Here are all of the bids, sorted by price descending: ")
    sorted_list = sorted(bids, key=lambda x: x[2], reverse = True)
    print_bids(sorted_list)
    
    print("\n" + "The Auction is for" , f"${total_offering_fv:13,.2f}", " of bonds." + "\n")
    
    # Calculation for YTM and number of successful bids
    
    # Loop to see which bids are successful
    count = 0
    tick = 0
    for bid in sorted_list:
        if (tick < total_offering_fv):
            count += 1
            tick += float(sorted_list[bid][1])
            pv = float(sorted_list[bid][2])
        else:
            sorted_list[bid][1] = 0
            
    # Calculate the YTM
    ytm = bond_yield_to_maturity(total_offering_fv, c, n, m, pv)

    print(count + " bids were successful in the auction."
          + "The auction clearing price was ${bid_price:8.2f}, i.e., YTM is" +
          ytm + " per year." + "\n" +
          "Here are the results for all bids: ")

    
    print_bids(bids)
    
    

        
        
        



