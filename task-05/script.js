class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <nav class="Navigation_panel">
        <ul>
            <li><u><a href="index.html"><img src="../task-05/assets/navbar/logo.png" alt="Left Icon" class="logo"></a></u></li>
        </ul>
        <ul>
            <li><u><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q"><img src="../task-05/assets/navbar/spotify.png" alt="spotify" class="socials"></a></u></li>       
            <li><u><a href="https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA"><img src="../task-05/assets/navbar/youtube.svg" alt="youtube" class="socials"></a></u></li>
            <li><u><a href="https://twitter.com/Imaginedragons?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"><img src="../task-05/assets/navbar/twitter.svg" alt="twitter" class="socials"></a></u></li>
            <li><u><a href="https://www.instagram.com/imaginedragons/"><img src="../task-05/assets/navbar/instagram.svg" alt="instagram" class="socials"></a></u></li>
        </ul>
      </nav>
      `;
    }
}

customElements.define('main-header', Header);