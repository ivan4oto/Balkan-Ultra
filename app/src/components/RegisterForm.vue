<template>
  <div>
    <b-container class="p-3">
      <div>
        <h2 class="d-flex justify-content-center" v-if="activateUltra">
          Register for the 80k Ultra!
        </h2>
        <h2 class="d-flex justify-content-center" v-if="!activateUltra">
          Register for the 15k Skyrace!
        </h2>
        <b-button-group>
          <b-button variant="danger" @click="activateUltra = true"
            >80k ULTRA</b-button
          >
          <b-button variant="info" @click="activateUltra = false"
            >15k SKY</b-button
          >
        </b-button-group>
      </div>
      <div v-if="activateUltra">
        <b-form
          @submit="onSubmit"
          @reset="onReset"
          v-if="show"
          class="p-4 reg-form"
        >
          <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              placeholder="Enter email"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Names:" label-for="input-2">
            <b-form-input
              class="mb-2"
              id="input-2"
              v-model="form.firstname"
              required
              placeholder="First name"
            ></b-form-input>

            <b-form-input
              id="input-2"
              class="mb-2"
              v-model="form.secondname"
              required
              placeholder="Second name"
            ></b-form-input>

            <b-form-input
              id="input-2"
              class="mb-2"
              v-model="form.lastname"
              required
              placeholder="Last name"
            ></b-form-input>
          </b-form-group>

          <b-form-row align-h="start">
            <b-col cols="4">
              <b-form-group
                id="input-group-3"
                label="Gender:"
                label-for="input-3"
              >
                <b-form-select
                  id="input-3"
                  v-model="form.gender"
                  :options="genders"
                  required
                ></b-form-select>
              </b-form-group>
            </b-col>

            <b-col cols="4">
              <b-form-group
                label="Additional beds:"
                description="Допълнителни легла за спане в хижа Плевен"
              >
                <b-form-input type="number" placeholder="Extra beds">
                </b-form-input>
              </b-form-group>
            </b-col>
          </b-form-row>

          <b-row align-h="start">
            <b-col cols="8">
              <b-form-group
                label="Qualifying Race:"
                description="Моля поставете линк към резултати на състезания доказващи, че нема бедствате по чукарите."
              >
                <b-form-input type="url" v-model="raceLink"></b-form-input>
              </b-form-group>
            </b-col>
            <b-col cols="2">
              <b-button
                @click="addLink"
                size="sm"
                variant="outline-primary"
                class="mb-1"
                >Add Link</b-button
              >
              <b-button size="sm" variant="outline-danger" @click="removeLink"
                >Remove Link</b-button
              >
            </b-col>
          </b-row>

          <b-list-group v-for="link in form.raceLinks" v-bind:key="link">
            <b-list-group-item>{{ link }}</b-list-group-item>
          </b-list-group>

          <b-row class="justify-content-md-center pt-5">
            <b-button
              type="submit"
              variant="primary"
              class="mr-1"
              @click="submitForm()"
              >Submit</b-button
            >
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-row>
        </b-form>
      </div>

      <div v-if="!activateUltra">
        <b-form
          @submit="onSubmit"
          @reset="onReset"
          v-if="show"
          class="p-4 reg-form"
        >
          <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              placeholder="Enter email"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Names:" label-for="input-2">
            <b-form-input
              class="mb-2"
              id="input-2"
              v-model="form.firstname"
              required
              placeholder="First name"
            ></b-form-input>

            <b-form-input
              id="input-2"
              class="mb-2"
              v-model="form.secondname"
              required
              placeholder="Second name"
            ></b-form-input>

            <b-form-input
              id="input-2"
              class="mb-2"
              v-model="form.lastname"
              required
              placeholder="Last name"
            ></b-form-input>
          </b-form-group>

          <b-form-row align-h="start">
            <b-col cols="4">
              <b-form-group
                id="input-group-3"
                label="Gender:"
                label-for="input-3"
              >
                <b-form-select
                  id="input-3"
                  v-model="form.gender"
                  :options="genders"
                  required
                ></b-form-select>
              </b-form-group>
            </b-col>

            <b-col cols="4">
              <b-form-group
                label="Additional beds:"
                description="Допълнителни легла за спане в хижа Плевен"
              >
                <b-form-input type="number" placeholder="Extra beds">
                </b-form-input>
              </b-form-group>
            </b-col>
          </b-form-row>

          <b-list-group v-for="link in form.raceLinks" v-bind:key="link">
            <b-list-group-item>{{ link }}</b-list-group-item>
          </b-list-group>

          <b-row class="justify-content-md-center pt-5">
            <b-button
              type="submit"
              variant="primary"
              class="mr-1"
              @click="submitForm()"
              >Submit</b-button
            >
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-row>
        </b-form>
      </div>

      <!-- <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card> -->
    </b-container>
  </div>
</template>

<script>
const axios = require("axios").default;

export default {
  name: "RegisterForm",
  data() {
    return {
      activateUltra: true,
      raceLink: "",
      form: {
        email: "",
        firstname: "",
        secondname: "",
        lastname: "",
        gender: null,
        age: 20,
        extraBeds: 0,
        raceLinks: [],
      },
      genders: [{ text: "Select One", value: null }, "Male", "Female"],
      show: true,
    };
  },
  methods: {
    addLink() {
      if (this.form.raceLinks.length > 2) {
        alert("Стига толкос брат");
      } else {
        this.form.raceLinks.push(this.raceLink);
        this.raceLink = "";
      }
    },
    removeLink() {
      this.form.raceLinks.pop();
    },
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.firstname = "";
      this.form.secondname = "";
      this.form.lastname = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    submitForm() {
      axios
        .post("http://127.0.0.1:5000/athlete", {
          first_name: this.form.firstname,
          second_name: this.form.secondname,
          last_name: this.form.lastname,
          email: this.form.email,
          gender: this.form.gender,
          age: this.form.age,
          bonus_beds: this.form.extraBeds,
          link: this.form.raceLinks,
        })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.reg-form {
  border: 10px solid lightseagreen;
}
</style>
