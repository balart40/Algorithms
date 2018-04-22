package leLeetCodePackage;

import java.util.ArrayDeque;

class ListNode 
{
	int val;
	ListNode next;
	ListNode(int x) { val = x; }
}

public class addTwoNumbers {
	
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
    	ListNode result = new ListNode(0);
    	ListNode currentNodeL1 = l1;
    	ListNode currentNodeL2 = l2;
    	ListNode zeroNode = new ListNode(0);
    	ArrayDeque<ListNode> stackOfLnodes = new ArrayDeque<ListNode>();  
    	int carry = 0;
    	// Do first sum since they are non empty
    	if((currentNodeL1.val+currentNodeL2.val)>9)
    	{
    		carry = 1;
    		result.val = (currentNodeL1.val+currentNodeL2.val)-10;
    	}
    	else
    	{
    		result.val = (currentNodeL1.val+currentNodeL2.val);
    		carry=0;
    	}
    	stackOfLnodes.push(result);
    	while(currentNodeL1.next!=null || currentNodeL2.next!=null || carry!=0)
    	{
    		// check for L1
    		if(currentNodeL1.next!=null)
    		{
    			currentNodeL1 = currentNodeL1.next;
    		}
    		else
    		{
    			currentNodeL1 = new ListNode(0);
    		}
    		// check for L2
    		if(currentNodeL2.next!=null)
    		{
    			currentNodeL2 = currentNodeL2.next;
    		}
    		else
    		{
    			currentNodeL2 = new ListNode(0);
    		}
    		// do sum
    		if((currentNodeL1.val+currentNodeL2.val+carry)>9)
        	{
        		result.next = new ListNode((currentNodeL1.val+currentNodeL2.val+carry)-10);
        		carry = 1;
        		result = result.next;
        		stackOfLnodes.push(result);
        	}
    		else
    		{
    			result.next = new ListNode(currentNodeL1.val+currentNodeL2.val+carry);
    			carry = 0;
    			result =  result.next;
    			stackOfLnodes.push(result);
    		}
    	}
    	result  = stackOfLnodes.pop();
    	while(!stackOfLnodes.isEmpty())
    	{
    		result  = stackOfLnodes.pop();
    	}
    	return result;
    }
    /*
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode L1 = new ListNode(2);
		L1.next = new ListNode(4);
		L1.next.next =  new ListNode(3);
		
		ListNode L2 = new ListNode(5);
		L2.next =  new ListNode(6);
		L2.next.next = new ListNode(4);
		
		ListNode result;
		result = addTwoNumbers(L1,L2);

		System.out.print(result.val);
		while(result.next!=null)
		{
			result = result.next;
			System.out.print(result.val);
		}
	}

}
