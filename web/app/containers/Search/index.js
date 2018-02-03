/**
 *
 * SearchB
 *
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom'
import { Helmet } from 'react-helmet';
import { createStructuredSelector } from 'reselect';
import { compose } from 'redux';
import { push } from 'react-router-redux';
import { Tabs, Icon, Spin, Button, Avatar } from 'antd';

import injectSaga from 'utils/injectSaga';
import injectReducer from 'utils/injectReducer';
import SearchBar from 'components/SearchBar';
import SearchHeader from 'components/SearchHeader';
import ResultsList from 'components/ResultsList';
import Footer from 'components/Footer';
import NoResultsFound from 'components/NoResultsFound';
import Profiler from 'containers/Profiler';
import FoodProfile from 'containers/FoodProfile';
import { makeSelectLoggedIn } from 'containers/App/selectors';
import { login } from 'containers/App/actions';
import { clearFoodProfile } from 'containers/FoodProfile/actions';

import { makeSelectSearch,
  makeSelectSearchString,
  makeSelectSearchType,
  makeSelectSearchResults,
  makeSelectSearchLoading,
  makeSelectProfileSelected } from './selectors';
import { changeSearchString,
      changeSearchType,
      profileSelected,
      searchRefresh } from './actions';
import reducer from './reducer';
import saga from './saga';
import SearchWrapper from './SearchWrapper';

export class Search extends React.Component { // eslint-disable-line react/prefer-stateless-function
  handleClick(event) {
    return event;
  }
  handleTabChange(event) {
    this.props.onSearchTypeChange(event);
    this.props.onSearchRefresh();
  }
  handleSearchStringChange(event) {
    this.props.onChangeSearchString(event);
  }
  handleProfileSelected(profileInfo) {
    // console.log(profileInfo);
    this.props.dispatch(push(`/foodprofile/${profileInfo.SN}`, { profileInfo }));
    this.props.onProfileSelected(profileInfo);
  }
  handleBackButton() {
    this.props.onProfileSelected(null);
    this.props.onClearFoodProfile();
  }

  render() {
    const { profileInfo, loading, searchString, searchResults, searchType } = this.props;
    const loadingSpinner = <Icon type="loading" style={{ fontSize: 40 }} spin />;
    const items = searchResults.items ? searchResults.items : [];
    const noResultsFound = items.length === 0 && searchString.length > 0 && !loading;
    const nutrientResults = noResultsFound ?
      <NoResultsFound /> :
      <ResultsList onProfileSelected={(profileData) => this.handleProfileSelected(profileData)} results={items} />;
    const nutrientResultsView = loading ?
    (<div className="loading-spinner">
      <Spin indicator={loadingSpinner} />
    </div>) : nutrientResults;
    const profilerProps = {
      onProfileSelected: (profileData) => this.handleProfileSelected(profileData),
      searchType,
    };
    const TabPane = Tabs.TabPane;
    const tabs = (
      <Tabs
        className="tab-bar"
        defaultActiveKey="all"
        activeKey={this.props.searchType}
        onChange={(e) => this.handleTabChange(e)}
      >
        <TabPane tab={<span><Icon type="home" />All</span>} key="all">
          {nutrientResultsView}
        </TabPane>
        <TabPane tab={<span><Icon type="file" />Nutrients</span>} key="nutrients">
          {nutrientResultsView}
        </TabPane>
        <TabPane tab={<span><Icon type="bars" />Profiler</span>} key="profiler">
          <Profiler {...profilerProps} />
        </TabPane>
        <TabPane tab={<span><Icon type="api" />Recipes</span>} key="recipes">
        </TabPane>
        <TabPane tab={<span><Icon type="book" />Wiki</span>} key="wiki">
        </TabPane>
      </Tabs>
    );
    const searchBarProps = {
      onClick: this.handleClick(),
      placeholder: 'Search for food',
      value: this.props.searchString,
      onChange: (event) => this.handleSearchStringChange(event),
      profileInfo,
    };
    const foodProfileProps = {
      profileHeader: profileInfo,
    };
    const user = 'D';
    const avatarStyle = {
      backgroundColor: '#7F3FBF',
      position: 'absolute' };
    const helmet = (
      <Helmet>
        <title>Search</title>
        <meta name="description" content="Nutry - Search" />
      </Helmet>);
    const searchView = (
      <div className="tabs" >
        {tabs}
      </div>
    );
    const profileView = (
      <div className="profileView">
        <FoodProfile {...foodProfileProps} />
      </div>
    );
    const mainView = profileInfo ? profileView : searchView;
    const backButton = (
      <Button type="primary" onClick={() => this.handleBackButton()} >Back</Button>
      );
    const backButtonView = (
      <div className="back-button" >
        { profileInfo ? backButton : null }
      </div>
    );
    const loginView = (
      <div className="sign-in-wrapper">
        { this.props.loggedIn ?
          <Avatar style={avatarStyle} size="default" >
            {user}
          </Avatar>
          : <Button type="primary" onClick={this.props.onLogin} >Sign In</Button> }
      </div>
    );
    const searchBarView = profileInfo ?
      null :
      <SearchBar {...searchBarProps} />;
    const searchHeaderProps = {
      loginView,
      searchBarView,
      backButtonView,
    };
    return (
      <SearchWrapper>
        {helmet}
        <SearchHeader {...searchHeaderProps} />
        {mainView}
        <Footer />
      </SearchWrapper>
    );
  }
}

Search.propTypes = {
  searchString: PropTypes.string.isRequired,
  searchResults: PropTypes.object.isRequired,
  loading: PropTypes.bool.isRequired,
  onChangeSearchString: PropTypes.func,
  loggedIn: PropTypes.bool,
  onLogin: PropTypes.func,
  onSearchRefresh: PropTypes.func,
  onSearchTypeChange: PropTypes.func,
  onProfileSelected: PropTypes.func,
  profileInfo: PropTypes.object,
  searchType: PropTypes.string,
  onClearFoodProfile: PropTypes.func,
  dispatch: PropTypes.func,
};

const mapStateToProps = createStructuredSelector({
  search: makeSelectSearch(),
  searchType: makeSelectSearchType(),
  loading: makeSelectSearchLoading(),
  searchString: makeSelectSearchString(),
  searchResults: makeSelectSearchResults(),
  loggedIn: makeSelectLoggedIn(),
  profileInfo: makeSelectProfileSelected(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
    onChangeSearchString: (evt) => dispatch(changeSearchString(evt.target.value)),
    onSearchTypeChange: (evt) => dispatch(changeSearchType(evt)),
    onSearchRefresh: () => dispatch(searchRefresh()),
    onLogin: () => dispatch(login()),
    onProfileSelected: (profileInfo) => dispatch(profileSelected(profileInfo)),
    onClearFoodProfile: () => dispatch(clearFoodProfile()),
  };
}

const withConnect = connect(mapStateToProps, mapDispatchToProps);

const withReducer = injectReducer({ key: 'search', reducer });
const withSaga = injectSaga({ key: 'search', saga });

export default compose(
  withReducer,
  withSaga,
  withConnect,
  withRouter,
)(Search);
