<div class="container">
  <div class="info">Info box</div>

  <form class="form" action="http://localhost:5000/login" method="post">
    <div class="element">
      <label for="login">Username</label>
      <input type="text" id="login" name="login" />
    </div>
    <div class="element">
      <label for="password">Password</label>
      <input type="password" id="password" name="password" />
    </div>

    <input type="submit" value="SING IN" />
  </form>
</div>

<style>
  button:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  button:hover {
    background-color: var(--btn-hov-color);
  }
  button {
    color: white;

    background-color: var(--btn-color);
    border: 0;
    padding-top: 8px /* 8px */;
    padding-bottom: 8px /* 8px */;
    border-radius: 4px /* 4px */;
    font-size: 1.125rem /* 18px */;
    line-height: 1.75rem /* 28px */;
    padding-left: 24px /* 24px */;
    padding-right: 24px /* 24px */;
  }
  input:focus {
    --tw-ring-color: rgb(199, 210, 254);
    border-color: var(--btn-hov-color);
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0
      var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0
      calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow),
      var(--tw-shadow, 0 0 #0000);
  }
  input {
    transition-property: background-color, border-color, color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 200ms;
    line-height: 2rem;
    padding-left: 12px /* 12px */;
    padding-right: 12px /* 12px */;

    padding-top: 4px /* 4px */;
    padding-bottom: 4px /* 4px */;
    color: rgb(55, 65, 81);
    font-size: 1rem /* 16px */;
    line-height: 1.5rem /* 24px */;
    width: 100%;
    background-color: white;
    border-radius: 4px;
    border: 1px solid rgb(209, 213, 219);
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  label {
    line-height: 1.75rem /* 28px */;
    font-size: 0.875rem /* 14px */;
    color: var(--font-color);
  }
  div.element {
    position: relative;
    margin-bottom: 16px;
    width: 75%;
  }
  @media (min-width: 768px) {
    form.form {
      width: 50%;
    }
  }
  @media (min-width: 1024px) {
    form.form {
      width: 33.333333%;
    }
  }
  form.form {
    background-color: var(--divs-color);
    border-radius: 8px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 30%;
    margin-top: 40px;
    position: relative;
    z-index: 10;
    --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  div.info {
    width: 100%;
    height: 48px;
    --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    margin: 0;
    margin-bottom: 80px;
    display: none;
  }
  div.container {
    display: flex;
    width: 100%;
    flex-direction: column;
    align-items: center;
  }
</style>
