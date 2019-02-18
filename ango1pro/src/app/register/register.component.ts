import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [UserService]
})
export class RegisterComponent implements OnInit {

  register;


  constructor(private userService: UserService) {}

  ngOnInit() {
    this.register = {
      username: '',
      password: '',
      email: ''
    };

  }

  registerUser() {
this.userService.registerNewUser(this.register).subscribe(
  response => {
    alert('User ' + this.register.username + ' has been created!' );
  },
  error => console.log('error', error)
);
  }

}
