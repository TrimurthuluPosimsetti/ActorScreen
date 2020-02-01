from django import forms  

class ScreenTimeForm(forms.Form):  
    files = forms.FileField() # for creating file input  


class output{
    public void readAndWriteOur(String x,String y){
FileInputStream instream = null;
	FileOutputStream output = null;
 
    	    File infile =new File("x");
    	    File outfile =new File("y");
 
    	    instream = new FileInputStream(infile);
    	    output = new FileOutputStream(outfile);
 
    	    byte[] buffer = new byte[1024];
 
    	    int length;
    	    /*copying the contents from input stream to
    	     * output stream using read and write methods
    	     */
    	    while ((length = instream.read(buffer)) > 0){
    	    	output.write(buffer, 0, length);
    	    }

    	    //Closing the input/output file streams
    	    instream.close();
    	    output.close();

}