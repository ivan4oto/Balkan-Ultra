<template>
  <div>
    <b-card
      overlay
      img-src="../assets/pictures/80banner.jpg"
      img-alt="Card Image"
      text-variant="white"
      class='text-right'
      title=""
      sub-title=""
    >
      <h1 id='card-txt'>78км УЛТРА</h1>
      <h2 id='card-txt-small'>6100м положителна денивелация</h2>
    </b-card>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="p-4 reg-form">
      <b-row>
        <b-col>
          <b-form-group id="input-group-1" label="Електронна поща:" label-for="input-1">
            <b-form-input id="input-1" v-model="form.email" type="email" required placeholder="Въведи поща"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-group id="input-group-1" label="Телефонен номер:" label-for="input-1">
            <b-form-input v-model="form.phone_number" type="text" maxlength="15" required placeholder="Въведи телефон за връзка"></b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <b-form-group id="input-group-2" label="Имена:" label-for="input-2">
        <b-row>
          <b-col sm>
            <b-form-input id="input-2" v-model="form.firstname" required placeholder="Първо име"></b-form-input>
          </b-col>
          <b-col sm>
            <b-form-input id="input-2" v-model="form.secondname" required placeholder="Бащино име"></b-form-input>
          </b-col>
          <b-col sm>
            <b-form-input id="input-2" v-model="form.lastname" required placeholder="Фамилия"></b-form-input>
          </b-col>        
        </b-row>
      </b-form-group>

      <b-row>
          <b-col sm>
            <b-form-group id="input-group-3" label="Пол:" label-for="input-3">
              <b-form-select id="input-3" v-model="form.gender" :options="genders" required></b-form-select>
            </b-form-group>
          </b-col>

          <b-col sm>
            <b-form-group label="Възраст:" description="Няма да се срамуваш!">
              <b-form-input type="number" min="0"  max="120"  v-model="form.age"></b-form-input>
            </b-form-group>
          </b-col>    
        
          <b-col sm>
            <b-form-group label="Допълнителни легла:" description="Допълнителни легла за спане в хижа Плевен">
              <b-form-input type="number" min="0"  max="7" placeholder="Брой допълнителни легла" v-model="form.extraBeds"></b-form-input>
            </b-form-group>
          </b-col>
        
      </b-row>
      <b-form-group
        label="Линк към резултати:"
        description="Моля поставете линк към резултати от две състезания надхвърлящи 4000м положителна денивелация всяко."
      >   
        <b-row align-h="start">     
            <b-col sm>
                <b-form-input type="url" v-model="raceLink"></b-form-input>
            </b-col>
          <b-col sm>
            <b-button class='m-1' @click="addLink" variant="outline-primary">Добави линк</b-button>
            <b-button class='m-1' variant="outline-danger" @click="removeLink">Премахни линк</b-button>
          </b-col>
        </b-row>
      </b-form-group>
      <b-row>
        <b-list-group v-for="link in form.raceLinks" v-bind:key="link">
          <b-list-group-item>{{ link }}</b-list-group-item>
        </b-list-group>
      </b-row>

      <b-row class='text-center'>
        <b-col>
          <b-button type="submit" variant="primary" class="mr-1">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-col>
      </b-row>
    </b-form>
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
        distance: "ultra",
        email: "",
        phone_number: "",
        firstname: "",
        secondname: "",
        lastname: "",
        gender: null,
        age: 0,
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
      this.submitForm();
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.firstname = "";
      this.form.secondname = "";
      this.form.lastname = "";
      this.raceLinks = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    submitForm() {
      axios
        .post(this.api_uri['athlete'], {
          first_name: this.form.firstname,
          second_name: this.form.secondname,
          last_name: this.form.lastname,
          email: this.form.email,
          phone_number: this.form.phone_number,
          gender: this.form.gender,
          age: this.form.age,
          bonus_beds: this.form.extraBeds,
          link: this.form.raceLinks,
          distance: this.form.distance
        })
       .then(
          (response)=> {
            console.log(response)
            if(response['data'] == "Success. Everything is fine!"){
              this.$router.push("Success")
            } else {
              alert("Възникна проблем. Моля, свържете се с нас.")
            }
        })
        .catch(function(error) {
          console.log(error);
          alert('Възникна проблем при изпращането на вашата регистрация. Моля, опитайте отново, или се свържете с нас нашата фейсбук страница.')
        });
    },
  },
};
</script>

<style scoped>
.reg-form {
  border: 3px solid rgb(150, 17, 0);
}

#card-txt-small {
  color: rgb(235, 119, 84);
  font-family: 'SPArielBG';
  margin-right: 5%;
  font-size: 2vw;
}
#card-txt{
  font-family: 'SPArielBG';
  font-weight: bold;
  font-style: italic;
  color: rgb(241, 60, 28);
  font-size: 7vw;
  margin-right: 5%;
}
</style>
