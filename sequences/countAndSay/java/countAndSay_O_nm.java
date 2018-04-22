package oracle_int_prep_pkg;

public class lookandsay {

	public static String counterModChain(String leWildChain)
	{
		System.out.println("\nChain to process: "+leWildChain);
		String chainToReturn = new String();
		String copyOfChain = leWildChain;
		char currentChar;
		char prevchar = leWildChain.charAt(0);
		int count = 1;
		if(leWildChain.length() == 1)
		{
			chainToReturn = new StringBuilder().append("1").append(leWildChain).toString();
			System.out.println("Returning: "+chainToReturn);
			return chainToReturn;
		}
		copyOfChain = copyOfChain.substring(1, copyOfChain.length());
		while(!copyOfChain.isEmpty())
		{
			currentChar = copyOfChain.charAt(0);
			copyOfChain = copyOfChain.substring(1, copyOfChain.length());
			if(currentChar != prevchar)
			{
				chainToReturn += new StringBuilder().append(String.valueOf(count)).append(prevchar);
				count = 1;
				prevchar = currentChar;
				if(copyOfChain.isEmpty())
				{
					chainToReturn += new StringBuilder().append(String.valueOf(count)).append(currentChar).toString();
					System.out.println("Returning: "+chainToReturn);
					return chainToReturn;
				}
			}
			else if(currentChar ==  prevchar)
			{
				count++;
				if(copyOfChain.isEmpty())
				{
					chainToReturn += new StringBuilder().append(String.valueOf(count)).append(currentChar).toString();
					System.out.println("Returning: "+chainToReturn);
					return chainToReturn;
				}
			}
		}
		System.out.print("Returning: "+chainToReturn);
		return  chainToReturn;
	}
	
	public static String countAndSay(int n)
	{
		String chain = "1";
		for(int i=1;i<n;i++)
		{
			chain = counterModChain(chain);
		}
		return chain;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String output =  countAndSay(6);
		System.out.println("\n"+output);
	}

}
