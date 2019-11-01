// For running clientside callbacks in plotly dash
// This is the top level file for all custom js functions.


var countTime = 750;  // the time needed to count up to all numbers in the app animations
var countTimeSlow=3000;


if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.clientside = {
    // Animate the about page stats
    // See count.js for more details
    countStatsClientsideFunction: function (pathname, sliderValue, id1, id2, id3, id4, hiddenId1, hiddenId2, hiddenId3, hiddenId4) {
        if (pathname == "/by_analysis"){
            animatedCount(id1, hiddenId1, countTime)
            animatedCount(id2, hiddenId2, countTime)
            animatedCount(id3, hiddenId3, countTime)
            animatedCount(id4, hiddenId4, countTime)
        }
    },

    // Animate the burger menu on mobile
    // see burger.js for more detials.
    animateBurgerOnClickClientsideFunction: function (activateId, triggerNClicks) {
        animateBurgerOnClick(activateId, triggerNClicks);
    },


    // counting stats on the by degree menu
    countPerDegreeStatsClientsideFunction: function (
        pathname,
        id1,
        id2,
        id3,
        id4,
        id5,
        id6,
        id7,
        id8,
        id9,
        id10,
        hiddenId1,
        hiddenId2,
        hiddenId3,
        hiddenId4,
        hiddenId5,
        hiddenId6,
        hiddenId7,
        hiddenId8,
        hiddenId9,
        hiddenId10,

    ) {
        if (pathname == "/by_degree"){
            animatedCount(id1, hiddenId1, countTimeSlow)
            animatedCount(id2, hiddenId2, countTimeSlow)
            animatedCount(id3, hiddenId3, countTimeSlow)
            animatedCount(id4, hiddenId4, countTimeSlow)
            animatedCount(id5, hiddenId5, countTimeSlow)
            animatedCount(id6, hiddenId6, countTimeSlow)
            animatedCount(id7, hiddenId7, countTimeSlow)
            animatedCount(id8, hiddenId8, countTimeSlow)
            animatedCount(id9, hiddenId9, countTimeSlow)
            animatedCount(id10, hiddenId10, countTimeSlow)
        }
    },

}