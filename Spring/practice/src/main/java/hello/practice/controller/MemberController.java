package hello.practice.controller;

import hello.practice.domain.Member;
import hello.practice.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@Controller
public class MemberController {
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @PostMapping(value = "/members/new")
    @ResponseBody
    public Long create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        return memberService.join(member);
    }

    @GetMapping("/members")
    @ResponseBody
    public List<Member> list() {
        return memberService.findMembers();
    }

    @GetMapping("/members/{id}")
    @ResponseBody
    public Optional<Member> profile(@PathVariable Long id) {
        return memberService.findOne(id);
    }

    @DeleteMapping("/members/{id}")
    @ResponseBody
    public Long delete(@PathVariable Long id) {
        return memberService.withdraw(id);
    }
}
