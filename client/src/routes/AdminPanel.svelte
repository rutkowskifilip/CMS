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
      <button class="delete">Delete</button>
    </div>
  {/each}
  <div class="addHeaderElem">
    <div>
      <label for="name">Name:</label>
      <input type="text" name="name" id="name" />
    </div>
    <div>
      <label for="url">Url:</label>
      <input type="text" name="url" id="url" />
    </div>
    <div>
      <button type="submit">Add</button>
    </div>
  </div>
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
      <button class="delete">Delete</button>
    </div>
  {/each}
  <div class="addSliderElem">
    <div>
      <label for="name">Url:</label>
      <input type="text" name="url" id="url" />
    </div>
    <div>
      <label for="desc">Description:</label>
      <input type="text" name="desc" id="desc" />
    </div>
    <div>
      <button type="submit">Add</button>
    </div>
  </div>
</section>

<style>
  p.img {
    width: 33%;
  }
  button.save {
    background: green;
    color: white;
  }
  button.delete {
    background: red;
    color: white;
  }
  button {
    height: 50%;
    width: 64px;
    background: var(--btn-color);
    color: var(--font-color);
  }
  div.addHeaderElem,
  div.addSliderElem {
    width: 80%;
    padding: 16px;
    background-color: var(--divs-color);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 16px;
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
