
import java.io.*;
import java.util.*;
import java.time.*;
import java.time.format.*;

public class LogAnalyzer {

    public static void main(String[] args) {

        try {
            FileReader fr = new FileReader("../data/login_logs.txt");
            BufferedReader br = new BufferedReader(fr);

            
            HashMap<String, ArrayList<LocalDateTime>> failedLogs = new HashMap<>();

            DateTimeFormatter formatter =
                DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

            br.readLine();

            String line;

            while ((line = br.readLine()) != null) {

                String[] parts = line.split(",");

                String timestamp = parts[0];
                String ip = parts[1];
                String status = parts[2];

                LocalDateTime time =
                    LocalDateTime.parse(timestamp, formatter);

                if (status.equals("FAILED")) {

                    if (failedLogs.containsKey(ip)) {

                        failedLogs.get(ip).add(time);

                    } else {

                        ArrayList<LocalDateTime> times = new ArrayList<>();

                        times.add(time);

                        failedLogs.put(ip, times);
                    }
                }
            }

            br.close();

            System.out.println("===== LOGGUARD SECURITY REPORT =====");

            for (Map.Entry<String, ArrayList<LocalDateTime>> entry
                    : failedLogs.entrySet()) {

                String ip = entry.getKey();

                ArrayList<LocalDateTime> times = entry.getValue();

                boolean suspicious = false;

                for (int i = 0; i < times.size(); i++) {

                    int count = 0;

                    LocalDateTime start = times.get(i);

                    for (int j = i; j < times.size(); j++) {

                        LocalDateTime current = times.get(j);

                        Duration duration =
                            Duration.between(start, current);

                        if (duration.toMinutes() <= 10) {
                            count++;
                        }
                        else {
                            break;
                        }
                    }

                    if (count >= 5) {
                        suspicious = true;
                        break;
                    }
                }

                if (suspicious) {
                    System.out.println(ip + " : SUSPICIOUS ACTIVITY");
                }
                else {
                    System.out.println(ip + " : NORMAL");
                }
            }

        }
        catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
        catch (DateTimeParseException e) {
            System.out.println("Invalid timestamp format: " + e.getMessage());
        }
    }
}
