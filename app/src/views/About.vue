<template>
  <div class="about m-4">
    <b-container class='gpxbox'>
      <b-row class='text-center'><b-col><h2>Свали GPX track от тук</h2></b-col></b-row>
      <b-row class='text-center' align-h='center'>
        <b-col><b-button href="Balkan_Ultra.gpx" download variant="danger">Свали GPX 80k ULTRA</b-button></b-col>
        <b-col><b-button href="Balkan_Sky.gpx" variant="info">Свали GPX 13k SKY</b-button></b-col>
      </b-row>  
    </b-container>
    <b-container class='mt-3 p-3 text-center information reqs'>
      <b-row class="text-center">
        <b-col><h3>Условия за участие <strong>80k ULTRA</strong></h3></b-col>        
      </b-row>
      <b-row>
        <h6>1. Всеки от участниците трябва да има предоставена валидна планинска застраховка преди старта на състезанието.<br>
            2. Завършени две състезания с минимум 4000 метра D+ всяко за последните 3 години /период 2017 - 2020 г./. Дължината на състезанията е без значение.<br>
            3. Разполагате със собствено GPS устройство /часовник, pъчен GPS, мобилен телефон с планинарска карта/ и може да се ориентирате по предоставена GPS следа. Вграден чип в главата от Бил Гейтс не се приема.<br>
            4. Всякаква помощ извън контролните пунктове е забранена, и ако разберем ще трябва да ви дисквалифицираме.
        </h6>
      </b-row>
    </b-container>
    <b-container class='mt-3'>
      <b-img src='../assets/pictures/profile80.jpg' fluid alt="Fluid image"></b-img>
    </b-container>
    <b-container class='mt-3'>
      <b-img src='../assets/pictures/profile13.jpg' fluid alt="Fluid image"></b-img>
    </b-container>

    <b-container class='important'>
      <b-row align-h='center'>
        <h3 class="mt-3 mb-4 geartitle text-center">Задължителна екипировка (80км):</h3>
      </b-row>
      <b-row class='text-center' cols="1" cols-sm="2" cols-md="4" cols-lg="4" align-h='center'>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-raincoat-96.png" fluid alt="Fluid image"></b-img> <p><strong>Водонепромокаемо яке.</strong>Гледайте да не пропуска. Износена мембрана с 20к воден стълб, която пуска вода на петата минута няма да ви свърши работа, ако завали стабилно.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-jumper-64.png" fluid alt="Fluid image"></b-img> <p><strong>Блуза/термо бельо с дълъг ръкав.</strong> Ако е от вълна то ще ви пази топли дори и да се намокри.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-mitten-64.png" fluid alt="Fluid image"></b-img> <p><strong>Чифт ръкавици.</strong></p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-phonelink-ring-64.png" fluid alt="Fluid image"></b-img> <p><strong>Телефон със заредена батерия.</strong>Гледайте да не е на 5% батерия на хижа Левски от много селфита.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-headlamp-128.png" fluid alt="Fluid image"></b-img> <p><strong>Минимум два челника</strong></p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-near-me-64.png" fluid alt="Fluid image"></b-img> <p><strong>GPS навигационно устройство</strong> със зареден трак на трасето.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/gear/icons8-storm-64.png" fluid alt="Fluid image"></b-img> <p>В зависимост от метерологичната прогноза може да променим задължителната екипировка.</p></b-col>
      </b-row>
    </b-container>
    <b-container class='information'>
      <b-row align-h='center'>
        <h3 class="mt-3 mb-4 geartitle text-center">Още информация:</h3>
      </b-row>
      <b-row class='text-center' cols="1" cols-sm="2" cols-md="4" cols-lg="4">
        <b-col sm><b-img class='gearimg' src="../assets/icons/icons8-bed-100.png" fluid alt="Fluid image"></b-img><h4>Спане</h4> <p>Хижа Плевен предлага добри условия за спане, при регистрация ние ще ви запазим легло. Ако имате нужда от допълнителен брой легла, моля посочете във формата за регистрация. Около хижата има достатъчно голяма поляна за палаткуване, ако поради една или друга причина не може да отседнете в хижата.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/icons8-hamburger-100.png" fluid alt="Fluid image"></b-img><h4>Храна</h4><p>Също така хижа Плевен разполага с кухня и прясно приготвена храна, която може да закупите на място в столовата. Освен това ние ще осигурим паста парти вечерта преди състезанието и диня парти на финала.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/icons8-money-100.png" fluid alt="Fluid image"></b-img><h4>Такса</h4><p>Участието е безплатно. Ако събитието ви харесва и искате да ни подкрепите всеки има възможност да го направи в кутията за дарения, която ще бъде на видно място в столовата.</p></b-col>
        <b-col sm><b-img class='gearimg' src="../assets/icons/icons8-car-roof-box-100.png" fluid alt="Fluid image"></b-img><h4>Транспорт</h4><p>До хижа Плевен се стига след кратък 30 минутен преход от паркинга на ВЕЦ Видима. Ако не разполагате със собствен транспорт може да се комбинирате с някой от другите участници. Всъщност ултра маратонците не са толкова лоши хора и никой няма да ви открадне чорапите, докато спите в колата.</p></b-col>
      </b-row>
    </b-container>
    <b-container>
    <b-row class='mt-4'><h3>Карта на трасе 80км:</h3></b-row>
    <b-row><b-img src='../assets/pictures/map80.jpg' fluid alt="Fluid image"></b-img></b-row>
    <b-row class='mt-4'><h3>Карта на трасе 13км:</h3></b-row>
    <b-row><b-img src='../assets/pictures/map13.jpg' fluid alt="Fluid image"></b-img></b-row>
    </b-container>

  </div>
</template>

<style scoped>
  /* @media only screen 
  and (min-width : 1224px) {
    .gearimg{
      width:100%;
      max-width:60px;
      max-height: 60px;
    }
  } */
      .gearimg{
      width:100%;
      max-width:60px;
      max-height: 60px;
    }
  .important {
    background-color: rgb(247, 204, 176);
  }
  .information {
    background-color: rgb(255, 251, 228);
  }
  .white {
    color: rgb(86, 114, 112);
  }
  .reqs{
    background-color: rgb(247, 204, 176);
  }
  h3, h2, h6, p{
    font-family: 'SPArielBG';
  }
</style>
