<script defer>
  export let theme = "Light";
  export let changeColors = () => {};
  export let font = "";
  export let changeFont = () => {};
  export let fontSize = 1;
  export let changeSize = () => {};
  export let changeTheme = () => {};
  export let bgColor, fontColor, fontColor2, divsColor, divsColor2;
  // const changeColors = () => {
  //   props.changeColors(theme);
  // };
  function show() {
    document.querySelector("div.form").style.display = "flex";
    document.querySelector("#settingsBtn").style.display = "none";
  }
  function close() {
    document.querySelector("div.form").style.display = "none";
    document.querySelector("#settingsBtn").style.display = "block";
  }
  function open() {
    document.documentElement.style.setProperty("--content", "(click to open)");
    document.querySelector("div.themeCreator").style.display = "flex";
  }
  function closeTheme() {
    document.documentElement.style.setProperty("--content", "");
    document.querySelector("div.themeCreator").style.display = "none";
  }
</script>

<button id="settingsBtn" on:click={show}>Settings</button>
<div class="form">
  <div class="element">
    <label for="theme">Theme</label>
    <select name="theme" id="theme" bind:value={theme} on:change={changeColors}>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
    </select>
  </div>
  <div class="element">
    <label for="font">Font</label>
    <select name="font" id="font" bind:value={font} on:change={changeFont}>
      <option value="Arial" style="font-family: Arial"
        >Arial (sans-serif)</option
      >
      <option value="Verdana">Verdana (sans-serif)</option>
      <option value="Helvetica" style="font-family: Halvetica"
        >Helvetica (sans-serif)</option
      >
      <option value="Tahoma" style="font-family: Tahoma"
        >Tahoma (sans-serif)</option
      >
      <option value="Trebuchet MS" style="font-family: Trebuchet MS"
        >Trebuchet MS (sans-serif)</option
      >
      <option value="Times New Roman" style="font-family: Times New Roman"
        >Times New Roman (serif)</option
      >
      <option value="Georgia" style="font-family: Georgia"
        >Georgia (serif)</option
      >
      <option value="Garamond" style="font-family: Garamond"
        >Garamond (serif)</option
      >
      <option value="Courier New" style="font-family: Courier New"
        >Courier New (monospace)</option
      >
      <option value="Brush Script MT" style="font-family: Brush Script MT"
        >Brush Script MT (cursive)</option
      >
    </select>
  </div>
  <div class="element">
    <label for="fontSize">Font size</label>
    <input
      min="0.5"
      max="3"
      step="0.0001"
      type="range"
      id="fontSize"
      name="fontSize"
      bind:value={fontSize}
      on:input={changeSize}
    />
  </div>
  <div class="element">
    <p id="pTheme" on:click={open}>Theme creator</p>
    <div class="themeCreator">
      <div class="elem">
        <label for="bgColor">Background color:</label>
        <input
          type="color"
          id="bgColor"
          name="bgColor"
          bind:value={bgColor}
          on:input={changeTheme}
        />
      </div>
      <div class="elem">
        <label for="fontColor">Font color:</label>
        <input
          type="color"
          id="fontColor"
          name="fontColor"
          bind:value={fontColor}
          on:input={changeTheme}
        />
      </div>
      <div class="elem">
        <label for="fontColor2">Second font color:</label>
        <input
          type="color"
          id="fontColor2"
          name="fontColor2"
          bind:value={fontColor2}
          on:input={changeTheme}
        />
      </div>
      <div class="elem">
        <label for="divsColor">Blocks color:</label>
        <input
          type="color"
          id="divsColor"
          name="divsColor"
          bind:value={divsColor}
          on:input={changeTheme}
        />
      </div>
      <div class="elem">
        <label for="divsColor2">Second blocks color:</label>
        <input
          type="color"
          id="divsColor2"
          name="divsColor2"
          bind:value={divsColor2}
          on:input={changeTheme}
        />
      </div>
      <button on:click={changeColors}>GO BACK TO DEFAULT</button>
      <button on:click={closeTheme}>CLOSE</button>
    </div>
  </div>

  <button id="closeBtn" on:click={close}>CLOSE</button>
</div>

<style>
  :root {
    --content: "(click to open)";
  }
  p {
    color: var(--font-color);
  }
  p#pTheme::after {
    content: var(--content);
  }
  div.themeCreator {
    display: none;
    flex-direction: column;
    width: 100%;
    align-items: left;
  }
  div.elem {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  input[type="color"] {
    width: 30px;
    height: 30px;
    padding: 0;
  }
  button:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  button:hover {
    background-color: var(--btn-hov-color);
  }
  button {
    color: white;
    margin-top: 5px;
    background-color: var(--btn-color);
    border: 0;
    padding-top: 8px /* 8px */;
    padding-bottom: 8px /* 8px */;
    border-radius: 4px /* 4px */;
    font-size: 1.125rem /* 18px */;
    line-height: 28px /* 28px */;
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
  input,
  select {
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
    div.form {
      width: 50%;
    }
  }
  @media (min-width: 1024px) {
    div.form {
      width: 33.333333%;
    }
  }
  div.form {
    overflow-y: scroll;
    height: 60%;
    display: none;
    position: fixed;
    left: 25%;
    background-color: var(--divs-color);
    border-radius: 8px;
    padding: 32px;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    width: 50%;
    max-height: calc(100% - 80px);
    z-index: 30;
    --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  button#settingsBtn {
    position: fixed;
    left: 10px;
    top: 10px;
    z-index: 20;
  }
  button#closeBtn {
    z-index: 20;
  }
</style>
