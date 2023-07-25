<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Log in</title>
    <link rel="stylesheet" href="login.css" />
    <link
      href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
      rel="stylesheet"
    />
  </head>
  <body>

  <!-- log in -->

  <div class="wrapper">
    <span class="icon-close"><i class='bx bx-plus-medical'></i></span>
    <div class="form-box login">
      <h2>Login</h2>
      <form action="validate.php" method="post">
        <div class="input-box">
          <span class="icon"> <i class='bx bxs-user'></i></span>
          <label>Username</label>
          <input type="text" name="usname" required>
        </div>

        <div class="input-box">
          <span class="icon"><i class='bx bxs-lock-alt'></i></span>
          <label>Password</label>
          <input type="password" name="pass" required>
        </div>

        <div class="remember-forget">
          <label><input type="checkbox">Remember me</label>
          <a href="#">Forget Password?</a>
        </div>
        <button type="submit" class="btn">Login</button>

        <div class="login-register">
          <p>Dont't have an account?<a href="#" class="register-link">Register</a></p>
        </div>
      </form>
    </div>


    <!-- Registration  -->

    <div class="form-box register">
      <h2>Registration</h2>
      <form action="connect.php" method="post">
        <div class="input-box">
          <span class="icon"> <i class='bx bxs-user'></i></span>
          <label>Username</label>
          <input type="text" name="usname" required>
        </div>

        <div class="input-box">
          <span class="icon"> <i class='bx bx-envelope'></i></span>
          <label>Email</label>
          <input type="email" name="email" required>
        </div>

        <div class="input-box">
          <span class="icon"><i class='bx bxs-lock-alt'></i></span>
          <label>Password</label>
          <input type="password" name="pass" required>
        </div>

        <div class="remember-forget">
          <label><input type="checkbox">Agree to terms & conditions</label>
         
        </div>
        <button type="submit" class="btn">Register</button>

        <div class="login-register">
          <p>Already have an account?<a href="#" class="login-link">Login</a></p>
        </div>
      </form>
    </div>


  </div>


    <script src="login.js"></script>
  </body>
</html>
