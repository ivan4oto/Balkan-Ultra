<template>
  <div class="m-3">
    <b-card
      overlay
      img-src="../assets/pictures/men.jpg"
      img-alt="Card Image"
      text-variant="white"
      class='text-left'
      title=""
      sub-title=""
    >
      <h1 id='card-txt-male'>МЪЖЕ</h1>
    </b-card>
      <div>
        <b-table
          small
          outlined
          striped
          responsive
          table-variant: dark
          text: info
          hover
          :items="mResults"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
      <b-card
      overlay
      img-src="../assets/pictures/women.jpg"
      img-alt="Card Image"
      text-variant="white"
      class='text-left'
      title=""
      sub-title=""
    >
      <h1 id='card-txt-male'>ЖЕНИ</h1>
    </b-card>

      <div>
        <b-table
          small
          outlined
          striped
          responsive
          hover
          table-variant: dark
          :items="fResults"
          :fields="fields"
        ></b-table>
      </div>
  </div>
</template>
<script>
export default {
  name: "ResultsTable",
  data() {
    return {
      fields: [
        {
          key: "Ranking",
          sortable: true,
        },
        {
          key: "First name",
          sortable: true,
        },
        {
          key: "Family name",
          sortable: false,
        },
        {
          key: "Time",
          // Variant applies to the whole column, including the header and footer
          variant: "",
        },
      ],
      mResults: [],
      fResults: [],
    };
  },
  methods: {
  
  },
  mounted: function() {
    var fResults = require("../assets/fresults.json");
    var mResults = require("../assets/mresults.json");
    this.fResults = fResults;
    this.mResults = mResults;
  },
};
</script>

<style scoped>
#card-txt-male{
  font-family: 'SPArielBG';
  font-weight: bold;
  font-style: italic;
  color: rgb(235, 166, 37);
  font-size: 7vw;
  margin-right: 5%;
}
</style>
