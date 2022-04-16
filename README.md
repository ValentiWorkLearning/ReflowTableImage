## Build
```shell
make BR2_EXTERNAL=${REPO_ROOT} -C buildroot O=${REPO_ROOT}/image_build/ orange_table_defconfig
```
## DTS Spi overlay
```dts
&spi1 {
	status = "okay";

        temp-sensor@1 {
            compatible = "maxim,max6675";
            reg = <0>;
            spi-max-frequency = <4300000>;
            spi-cpha;
        };

};
```


## Boot from NFS:
Device console:
```shell
setenv bootargs console=${console} root=/dev/nfs rootfstype=nfs ip=dhcp nfsvers=3 nfsroot=192.168.0.126:/nfs/orange_zero_rootfs
run bootargs
```

Completed image build:
## Example
```shell
sudo tar -xavf /path/to/output_dir/rootfs.tar -C /path/to/nfs_root_dir
```

## Host PC
```shell
cd images
sudo tar -xavf rootfs.tar -C /mnt/orange_zero_rootfs/
cd ..
```