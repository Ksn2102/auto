<template>
    <div class="back">
        <h1>Где нас найти?</h1>
    </div>
    <div class="conteiner1">
          
          <div class="line">
              <p class="fat">Телефон:</p>
              <p>8 336 898 45 56</p>
              
              <p>Звонок по России бесплатный</p>
          </div>
          <div class="conto">
              <div class="line">
                  <p class="fat">Email:</p>
                  <p>mail.ru</p>
              </div>
          </div>
          <div class="cont">
              <div class="line">
                  <p class="fat">CarPoint  </p>
                  <p>ул. Доваторцев, 44ж (1 этаж, главный вход)</p>
                
                  <p class="line">График работы: ежедневно с 11:00 до 21:00 без перерыва и выходных.</p>
              </div>
          </div>
      
          <div class="map">
            <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A7482b98600090461c57afa96e2323b4de1c7a1c0bbb80e83a33e707a9a84a4b7&amp;source=constructor" width="500" height="400" frameborder="0"></iframe>
          </div>

      </div>
</template>

<script>
export default {
    name: 'WherePage',
};
</script>
<style>
.back{
    background-color: rgb(100, 100, 197);
    margin-top: 45px;
    padding-left: 95px;
}

.linee{
    border-bottom: 1px solid black;
    text-align: center;
    padding-top: 30px;
}

.line{
    margin-top: 20px;
}

.conto{
    margin-top: 20px;
}

.fat{
    font-weight: bold;
}

.picture{
    width: 500px;
    margin-top: 30px;
}

.conteiner1 {
    max-width: 500px;
    width: 100%;
    margin: 0 auto;
}
</style>