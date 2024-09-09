
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class simonguzman {
    public static void main(String[] args) throws IOException{
        makeHttpRequest("https://www.google.com/");
    }

    public static void makeHttpRequest(String url) throws IOException{
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        
        con.setRequestMethod("GET");

        int responseCode = con.getResponseCode();
        if (responseCode == 200) {
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) { 
                response.append(inputLine);
            }
            in.close();

            System.out.println(response.toString());
        }else{
            System.out.println("ERROR: "+responseCode);
        }
    }
}
