
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class WeatherController {

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @PostMapping("/checkBalance")
    public String checkBalance(@RequestParam("account") String account, Model model) {
        // Fake logic for demo
        if (account.equals("12345")) {
            model.addAttribute("balance", 1000);
        } else {
            model.addAttribute("error", "Account not found.");
        }
        return "index";
    }
}
