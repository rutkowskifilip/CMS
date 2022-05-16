<script>
  import { getContext } from "svelte";

  const headerElems = getContext("headerElems");
  console.log(headerElems);
  const slides = getContext("slides");
  export let sliderChangeTimeFromChild;

  export let changeTime = () => {};
</script>

<section>
  <p>Header</p>
  {#each headerElems as elem}
    <div class="elem">
      <p>{elem.name}</p>
      <h2>"{elem.url}"</h2>
    </div>
  {/each}
  <form
    class="addHeaderElem"
    action="http://localhost:5000/addelement"
    method="post"
  >
    <p>Add header element</p>
    <div class="elem">
      <label for="name">Name:</label>
      <input type="text" name="name" id="name" />
    </div>
    <div class="elem">
      <label for="url">Url:</label>
      <input type="text" name="url" id="url" />
    </div>
    <input type="submit" value="ADD" />
  </form>
  <form
    action="http://localhost:5000/deleteelement"
    method="post"
    class="deleteHeaderElem"
  >
    <p>Delete header element</p>
    <div class="elem">
      <p>Podaj nazwę elementu do usunięcia</p>
      <input type="text" name="delName" id="delName" />
    </div>
    <div class="elem">
      <p>Podaj zawartość elementu</p>
      <input type="text" name="delText" id="delText" />
    </div>
    <input type="submit" value="DELETE" />
  </form>
</section>
<section>
  <p>Slider</p>
  <div class="elem">
    <label for="pace">Slider changing [s]:</label>

    <input
      id="sliderChangeTime"
      type="number"
      bind:value={sliderChangeTimeFromChild}
      on:change={changeTime}
    />
  </div>
  {#each slides as elem}
    <div class="elem">
      <p class="img" contenteditable="true">{elem.img}</p>
      <h2 contenteditable="true">"{elem.content}"</h2>
      <button class="save">Save</button>
    </div>
  {/each}

  <form
    class="addSliderElem"
    action="http://localhost:5000/addphoto"
    method="post"
  >
    <p>Add slider element</p>
    <div class="elem">
      <div>
        <label for="name">Link:</label>
        <input type="text" name="link" id="link" />
      </div>
      <div>
        <label for="url">Content:</label>
        <input type="text" name="content" id="content" />
      </div>
    </div>
    <input type="submit" value="ADD" />
  </form>
</section>
<section>
  <p>Users</p>
  <form action="http://localhost:5000/deleteuser" method="post" class="form">
    <p>Delete users</p>
    <div class="elem">
      <p>User login</p>
      <input type="text" name="delLogin" id="delLogin" />
    </div>

    <input type="submit" value="DELETE" />
  </form>

  <form action="http://localhost:5000/edituser" method="post" class="form">
    <p>Edit users</p>
    <div class="elem">
      <p>User login</p>
      <input type="text" name="editLogin" id="editLogin" />
    </div>
    <div class="elem">
      <p>User password</p>

      <input type="text" name="editPassword" id="editPassword" />
    </div>
    <div class="elem">
      <p>New login</p>
      <input type="text" name="newLogin" id="newLogin" />
    </div>
    <div class="elem">
      <p>New passord</p>
      <input type="text" name="newPassword" id="newPassword" />
    </div>
    <input type="submit" value="SAVE" />
  </form>
</section>

<style>
  p.img {
    width: 33%;
  }
  button.save {
    background: green;
    color: white;
  }

  input[type="submit"]:focus,
  button:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
  }
  input[type="submit"]:hover {
    background-color: var(--btn-hov-color);
  }
  input[type="submit"],
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
  form.addHeaderElem,
  form.deleteHeaderElem,
  form.addSliderElem {
    width: 80%;
    padding: 16px;
    background-color: var(--divs-color);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-top: 16px;
  }
  form.form {
    width: 80%;
    padding: 16px;
    background-color: var(--divs-color);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-top: 16px;
    align-content: center;
  }
  section {
    margin-bottom: 96px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  div.elem {
    margin-top: 16px;
    margin-bottom: 16px;
    width: 80%;
    background-color: var(--divs-color2);
    padding: 16px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-radius: 8px;
  }

  h2 {
    letter-spacing: 0.1em;
    font-size: 0.75rem /* 12px */;
    font-weight: 500;
    color: var(--font-color);
  }
</style>
