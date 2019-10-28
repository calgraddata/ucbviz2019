// For running clientside callbacks in plotly dash
// This is the top level file for all custom js functions.


var countTime = 5000;  // the time needed to count up to all numbers in the app animations


if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.clientside = {
    // Animate the about page stats
    // See count.js for more details
    countStatsClientsideFunction: function (pathname, id1, hiddenId1) {
        if (pathname == "/by_analysis"){
            animatedCount(id1, hiddenId1, countTime)
//            animatedCount(id2, hiddenId2, countTime)
//            animatedCount(id3, hiddenId3, countTime)
        }
    },

    // Animate the burger menu on mobile
    // see burger.js for more detials.
    animateBurgerOnClickClientsideFunction: function (activateId, triggerNClicks) {
        animateBurgerOnClick(activateId, triggerNClicks);
        return ""
    }

}