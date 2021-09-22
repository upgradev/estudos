package com.example.SpringBootSample.controller;

import java.util.Locale;
import java.util.Map;

import com.example.SpringBootSample.application.service.UserApplicationService;
import com.example.SpringBootSample.form.GroupOrder;
import com.example.SpringBootSample.form.SignupForm;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.extern.slf4j.Slf4j;

@Controller
@RequestMapping("/user")
@Slf4j // Annotating this class provides a static variable called "log".
public class SignupController {

    @Autowired
    private UserApplicationService userApplicationService;

    // display the user signup screen
    @GetMapping("/signup")
    public String getSignup(Model model, Locale locale, @ModelAttribute SignupForm form) {

        // get gender
        Map<String, Integer> genderMap = userApplicationService.getGenderMap(locale);
        model.addAttribute("genderMap", genderMap);

        return "user/signup";
    }

    // user signup process
    @PostMapping("/signup")
    public String postSignup(Model model, Locale locale, @ModelAttribute @Validated(GroupOrder.class) SignupForm form,
            BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            return getSignup(model, locale, form);
        }
        log.info(form.toString());
        return "redirect:/login";
    }
}