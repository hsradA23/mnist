<script>
  let arr = Array(28 * 28).fill(0);
  let pred = Array(10).fill(1);
  let p0 = 0;

  let clicked = false;
  document.body.onmousedown = function () {
    clicked = true;
  };
  document.body.onmouseup = function () {
    clicked = false;
    //console.log(arr);
  };

  const reset = () => {
    arr = Array(28 * 28).fill(0);
  };
</script>

<div>
  <div class="container">
    {#each arr as val}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-mouse-events-have-key-events -->
      <div
        class={val === 0 ? "child" : "childClicked"}
        on:click={() => {
          val = 1;
        }}
        on:mouseover={() => {
          if (clicked) {
            val = 1;

            fetch("http://0.0.0.0:9999/items/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(arr),
            })
              .then((response) => response.json())
              .then((data) => {
                pred = data["message"];
                pred = JSON.parse(pred);
                console.log(pred);
              })
              .catch((error) => {
                console.error("Error:", error);
              });
          }
        }}
      />
    {/each}
  </div>
  <button on:click={reset}>Clear</button>

  <div style="display: flex;">
    0 <div
      style="height: 10px; width: {305 * pred[0]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    1 <div
      style="height: 10px; width: {305 * pred[1]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    2 <div
      style="height: 10px; width: {305 * pred[2]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    3 <div
      style="height: 10px; width: {305 * pred[3]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    4 <div
      style="height: 10px; width: {305 * pred[4]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    5 <div
      style="height: 10px; width: {305 * pred[5]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    6 <div
      style="height: 10px; width: {305 * pred[6]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    7 <div
      style="height: 10px; width: {305 * pred[7]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    8 <div
      style="height: 10px; width: {305 * pred[8]}px; background-color: black;"
    />
  </div>
  <div style="display: flex;">
    9 <div
      style="height: 10px; width: {305 * pred[9]}px; background-color: black;"
    />
  </div>
</div>

<style>
  .container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;

    height: 300px;
    width: 300px;
    /*     
    -webkit-filter: blur(5px);
    -moz-filter: blur(5px);
    -o-filter: blur(5px);
    -ms-filter: blur(5px);
    filter: blur(5px);
   */

    border-style: solid;
    border-width: 2px;
    border-color: gray;
    border-radius: 5px;

    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none;
  }

  .child {
    flex: 1 0 calc(100% * (1 / 28)); /* explanation below */
    background-color: white;
    aspect-ratio: 1 / 1;
  }

  .childClicked {
    flex: 1 0 calc(100% * (1 / 28)); /* explanation below */
    background-color: black;
    aspect-ratio: 1 / 1;
    scale: 1.5;
    border-radius: 50%;
  }
  button {
    width: 305px;
  }
</style>
