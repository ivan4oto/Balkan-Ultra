<template>
  <div>
    <b-container class="d-flex justify-content-center">
      <b-img
        width="150"
        height="150"
        fluid
        alt="Fluid image"
        src="../assets/logo.jpg"
      />
    </b-container>
    <div>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Text slides with image -->
        <b-carousel-slide caption="" text="" img-src=""></b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide img-src="">
          <h1></h1>
        </b-carousel-slide>

        <!-- Slides with image only -->
        <b-carousel-slide img-src=""></b-carousel-slide>

        <!-- Slides with img slot -->
        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <b-carousel-slide>
          <template #img>
            <img
              class="d-block img-fluid w-100"
              width="1024"
              height="480"
              src=""
              alt="image slot"
            />
          </template>
        </b-carousel-slide>

        <!-- Slide with blank fluid image to maintain slide aspect ratio -->
        <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
          <p>
          </p>
        </b-carousel-slide>
      </b-carousel>

      <!-- <p class="mt-4">
        Slide #: {{ slide }}<br />
        Sliding: {{ sliding }}
      </p> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {},
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>

<style scoped></style>
