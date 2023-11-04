import java.net.*;
import java.io.*;

public class UDPmyServer {
    public static void main(String args[]) {
        byte b[] = new byte[3072];
        DatagramSocket dsoc = null;
        FileOutputStream f = null;

        try {
            dsoc = new DatagramSocket(1000);
            f = new FileOutputStream("C:\\Users\\Aniket\\Desktop\\Abhishek Python\\college\\cn\\practical codes\\udp\\server.txt");

            while (true) {
                DatagramPacket dp = new DatagramPacket(b, b.length);
                dsoc.receive(dp);
                f.write(dp.getData(), 0, dp.getLength());
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (dsoc != null) {
                dsoc.close();
            }
        }
    }
}
