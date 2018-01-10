import styled from 'styled-components';

const BannerWrapper = styled.div`
  background: white;
  width: 100%;
  height: 567px;
  .banner-wrapper {
    overflow: initial;
    position: relative;
    z-index: 1;
  }
  .home-page-wrapper {
    width: 100%;
    padding: 0;
    position: relative;
    color: #314659;
    font-family: 'SF UI Display', "Helvetica Neue For Number", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  .banner-bg-wrapper {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }
  .banner-bg-wrapper svg {
    fill: none;
  }
  .banner-bg {
    background: #7F3FBF;
    width: 120%;
    height: 200px;
    background: #7f3fbf;
    position: absolute;
    bottom: -150px;
    left: 0%;
    transform: translate(0px, 0px) rotate(-3.8243deg);

  }
  .banner-page {
    padding-top: 200px;
    padding-left: 50px;
    padding-bottom: 100px;
  }
  .banner-page h1 {
      font-size: 70px;
  }
  .banner-page span {
    font-size: 30px;
  }
  .buttons {
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    margin-top: 24px;
  }
  .buttons .btn {

  }
  .buttons .btn:hover {
    border-color: rgba(127, 63, 191,0.70);
    -webkit-box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.70);
    -moz-box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.60);
    box-shadow: 0px 4px 10px 0px rgba(127, 63, 191,0.70);
  }
  .btn {
    color: white;
    width: 200px;
    background: #7F3FBF;
    border-radius: 100px;
    margin-right:20px;
    border: none;
  }
  .btn:hover {
    color: black;
  }

`;

export default BannerWrapper;
