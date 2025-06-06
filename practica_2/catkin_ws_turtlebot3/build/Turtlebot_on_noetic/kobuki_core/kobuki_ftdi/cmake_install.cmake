# Install script for directory: /workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/workspace/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/workspace/catkin_ws/build/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/catkin_generated/installspace/kobuki_ftdi.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_ftdi/cmake" TYPE FILE FILES
    "/workspace/catkin_ws/build/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/catkin_generated/installspace/kobuki_ftdiConfig.cmake"
    "/workspace/catkin_ws/build/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/catkin_generated/installspace/kobuki_ftdiConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_ftdi" TYPE FILE FILES "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_ftdi" TYPE DIRECTORY FILES "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/bluetooth")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_ftdi" TYPE DIRECTORY FILES "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/eeproms")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/kobuki_ftdi" TYPE PROGRAM FILES
    "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/scripts/turtlebot_config"
    "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/scripts/create_udev_rules"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/kobuki_ftdi" TYPE FILE FILES "/workspace/catkin_ws/src/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/57-kobuki.rules")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/workspace/catkin_ws/build/Turtlebot_on_noetic/kobuki_core/kobuki_ftdi/src/cmake_install.cmake")

endif()

